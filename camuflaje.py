import re

def cargar_configuracion(ruta_archivo):
    """📂 Lee el archivo de configuración y extrae patrones válidos."""
    patrones = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                # 🧹 Ignorar líneas vacías y comentarios
                if linea and not linea.startswith('#'):
                    patrones.append(linea)
    except FileNotFoundError:
        print(f"⚠️ Archivo de configuración no encontrado en {ruta_archivo}")
    return patrones

def camuflar_texto(texto, patrones_config=[]):
    """🔒 Oculta IPs, usuarios y los patrones del archivo de configuración."""
    # 🌐 1. Ocultar direcciones IP
    patron_ip = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    texto_seguro = re.sub(patron_ip, '10.x.x.x', texto)
    
    # 👤 2. Ocultar nombres de usuario después de 'user:'
    texto_seguro = re.sub(r'(user:\s*)\S+', r'\1REDACTED', texto_seguro)
    
    # 📋 3. Aplicar patrones dinámicos de la configuración
    for patron in patrones_config:
        texto_seguro = texto_seguro.replace(patron, 'REDACTED')
        
    return texto_seguro

if __name__ == "__main__":
    # ⚙️ Cargar configuración modular externa
    patrones_extra = cargar_configuracion('examples/ejemplo_configuracion.txt')
    
    # 📖 Leer el archivo de entrada
    with open('examples/entrada.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    # 🔄 Procesar el texto aplicando todas las reglas
    texto_seguro = camuflar_texto(contenido, patrones_extra)
    
    # 💾 Escribir el resultado en el archivo de salida
    with open('examples/salida_camuflada.txt', 'w', encoding='utf-8') as archivo:
        archivo.write(texto_seguro)
        
    print("Proceso completado con éxito 📄.")

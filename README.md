# 🦎 El Camuflaje

Herramienta ligera en Python diseñada para preparar información técnica antes de compartirla, preservando la estructura útil y ocultando datos sensibles o internos.

## 💡 El Problema

Las configuraciones de servidores, logs y capturas de terminal pueden contener información que no debería hacerse pública, como direcciones IP, nombres de usuario, hostnames o rutas internas.

Compartir esta información sin filtrar puede exponer detalles innecesarios del entorno.

> **Regla fundamental:** No borrar información útil. Ocultar únicamente lo que no necesitas revelar.

## 🔄 ANTES ➔ DESPUÉS
```text
ANTES:

hostname: srv-produccion-clientex
IP: 10.42.15.23
user: admin-clientex
path: /home/admin-clientex
port: 5432
```
```
DESPUÉS:

hostname: srv-produccion-REDACTED
IP: 10.x.x.x
user: admin-REDACTED
path: /home/admin-REDACTED
port: 5432
```
La estructura y la información relevante se mantienen, mientras que los datos configurados para ser ocultados son reemplazados.

## 📁 Estructura del Proyecto
```
el-camuflaje/
│
├── camuflaje.py
├── README.md
├── LICENSE
├── .gitignore
│
├── examples/
│   ├── entrada.txt
│   ├── salida_camuflada.txt
│   └── ejemplo_configuracion.txt
│
└── tests/
    └── test_camuflaje.py
```

## 🚀 Uso

1. Configurar los patrones

- Define los patrones que deseas ocultar en:`examples/ejemplo_configuracion.txt`

2. Preparar la entrada

- Coloca la información técnica que deseas procesar en:`examples/entrada.txt`

3. Ejecutar la herramienta:`python3 camuflaje.py`

4. Revisar el resultado
- La información procesada se genera en:

`examples/salida_camuflada.txt`

## 🧪 Pruebas Automatizadas

Para verificar el funcionamiento de las reglas de redacción:

`python3 -m unittest discover tests`

## 🛡️ Características

🐍 Python puro: utiliza la biblioteca estándar de Python.

🐧 Orientado a Linux y OpSec: pensado para trabajar con información técnica de entornos Linux.

🧱 Sin dependencias externas: no requiere paquetes adicionales.

⚙️ Configurable: permite definir patrones personalizados mediante un archivo externo.

📋 Preserva la estructura: modifica únicamente la información que coincide con los patrones configurados.

🔒 Local: procesa la información en el propio equipo sin necesidad de servicios externos.


## ⚠️ Alcance y Limitaciones

- El Camuflaje es una herramienta de apoyo para reducir la exposición accidental de información técnica.

- No garantiza que toda la información sensible de un texto sea detectada automáticamente.

- La herramienta depende de los patrones definidos en su configuración, por lo que el resultado debe revisarse antes de compartir información públicamente.

> El Camuflaje ayuda a ocultar lo que le indiques. La revisión humana sigue siendo necesaria.

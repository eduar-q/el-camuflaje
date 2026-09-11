# 🎭 El Camuflaje

Herramienta ligera en Python diseñada para preparar y limpiar información técnica antes de compartirla, preservando la estructura útil y ocultando datos sensibles.

## 💡 El Problema
Las configuraciones de servidores, logs y capturas de terminal suelen contener datos internos que no deberían hacerse públicos (direcciones IP, nombres de usuario, hostnames, rutas). Compartir esta información sin filtrar puede convertirse en una fuga de datos.

> **Regla fundamental:** No borrar información útil. Ocultar únicamente lo que no necesitas revelar.

## 🔄 ANTES ➔ DESPUÉS

**ANTES:**
```text
hostname: srv-produccion-clientex
IP: 10.42.15.23
user: admin-clientex
path: /home/admin-clientex
port: 5432
```

**DESPUÉS:**
```text
hostname: srv-production-REDACTED
IP: 10.x.x.x
user: admin-REDACTED
path: /home/admin-REDACTED
port: 5432
```

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

1. Configura tus patrones personalizados en examples/ejemplo_configuracion.txt.

2. Coloca el texto a procesar en examples/entrada.txt.

3. Ejecuta el script principal: `python3 camuflaje`
4. Revisa el resultado seguro en examples/salida_camuflada.txt.

## 🧪 Pruebas Automatizadas

Para verificar el funcionamiento correcto de las reglas de redacción:
`
python3 -m unittest discover tests
`
## 🛡️ Características:

🐍 Desarrollado en Python puro.

🐧 Orientado a entornos Linux y OpSec.

🧱 Sin dependencias externas.

⚙️ Altamente configurable mediante archivos externos.



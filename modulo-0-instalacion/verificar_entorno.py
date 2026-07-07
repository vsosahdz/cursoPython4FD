"""
Verificador del entorno del taller "Python for Ford 2026".

Comprueba que tienes todo lo necesario para el taller y te dice, en español,
qué falta y cómo corregirlo.

Uso (en la terminal de VS Code, con el entorno .venv activado):

    python modulo-0-instalacion/verificar_entorno.py

No necesitas entender este código: solo ejecútalo. Si ves todo en ✅,
¡estás listo para el taller!
"""

import sys
import os

# Versión mínima de Python recomendada para el taller
PYTHON_MINIMO = (3, 9)

# Librerías necesarias:  nombre_para_importar -> (nombre_para_instalar, para_qué)
LIBRERIAS = {
    "pandas": ("pandas", "manejar tablas de datos"),
    "matplotlib": ("matplotlib", "crear gráficas"),
    "duckdb": ("duckdb", "hacer consultas tipo SQL"),
    "IPython": ("jupyter", "ejecutar notebooks"),
}

VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"


def ok(msg):
    print(f"{VERDE}✅ {msg}{RESET}")


def error(msg):
    print(f"{ROJO}✗ {msg}{RESET}")


def aviso(msg):
    print(f"{AMARILLO}   → {msg}{RESET}")


def main():
    print("=" * 60)
    print("  Verificando tu entorno para el taller Python for Ford 2026")
    print("=" * 60)
    print()

    problemas = 0

    # 1) Versión de Python -----------------------------------------------
    v = sys.version_info
    version_txt = f"{v.major}.{v.minor}.{v.micro}"
    if (v.major, v.minor) >= PYTHON_MINIMO:
        ok(f"Python {version_txt} instalado")
    else:
        problemas += 1
        error(f"Python {version_txt} es muy antiguo (se necesita "
              f"{PYTHON_MINIMO[0]}.{PYTHON_MINIMO[1]} o superior)")
        aviso("Instala la última versión desde https://www.python.org/downloads/")

    # 2) ¿Está activo un entorno virtual (.venv)? ------------------------
    en_venv = sys.prefix != sys.base_prefix
    if en_venv:
        ok("Entorno virtual (.venv) activo")
    else:
        aviso("Aviso: no parece haber un entorno virtual activo.")
        aviso("No es un error grave, pero se recomienda activar .venv:")
        aviso("   .venv\\Scripts\\activate    (Windows)")

    # 3) Librerías -------------------------------------------------------
    print()
    print("Revisando librerías necesarias:")
    for importar, (instalar, para_que) in LIBRERIAS.items():
        try:
            modulo = __import__(importar)
            version = getattr(modulo, "__version__", "?")
            ok(f"{instalar} {version}  ({para_que})")
        except ImportError:
            problemas += 1
            error(f"Falta '{instalar}'  ({para_que})")
            aviso(f"Instálalo con:  pip install {instalar}")
            aviso("O instala todo de una vez:  pip install -r requirements.txt")

    # 4) ¿Existe el dataset del taller? ----------------------------------
    print()
    carpeta_taller = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_ventas = os.path.join(carpeta_taller, "datos", "ventas.csv")
    ruta_conc = os.path.join(carpeta_taller, "datos", "concesionarios.csv")
    if os.path.exists(ruta_ventas) and os.path.exists(ruta_conc):
        ok("Datos del taller encontrados (ventas.csv y concesionarios.csv)")
    else:
        aviso("Aviso: no encontré los datos del taller en la carpeta 'datos/'.")
        aviso("Si es necesario, genéralos con:  python datos/generar_datos.py")

    # Resumen ------------------------------------------------------------
    print()
    print("=" * 60)
    if problemas == 0:
        print(f"{VERDE}🎉 ¡Tu entorno está listo para el taller!{RESET}")
        print("   Nos vemos en clase. No necesitas hacer nada más.")
    else:
        print(f"{ROJO}Faltan {problemas} cosa(s) por resolver.{RESET}")
        print("   Revisa los mensajes de arriba. Si te atoras, guarda una")
        print("   captura de pantalla y llévala a la sesión de dudas.")
    print("=" * 60)

    return 0 if problemas == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

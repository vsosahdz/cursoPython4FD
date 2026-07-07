# Módulo 0 — Instalación (PRE-TRABAJO) 🛠️

> **Esto se hace ANTES del taller.** El día del taller solo verificamos que todo
> quedó bien (unos 20 minutos). Si llegas con las herramientas instaladas,
> aprovechamos las 4 horas al 100%.
>
> **Sistema operativo:** estas instrucciones son para **Windows**.
> **Tiempo estimado:** 30–45 minutos.

Si te atoras en cualquier paso, no te preocupes: al final de esta guía hay una
sección de **Problemas comunes**, y tendrás la sesión de dudas para resolverlo.

---

## ¿Qué vamos a instalar y para qué?

| Herramienta | ¿Qué es? | ¿Por qué la usamos? |
|-------------|----------|---------------------|
| **Python** | El lenguaje de programación | Es el "motor" que ejecuta todo |
| **VS Code** | Un editor (como un Word para código) | Donde abriremos los notebooks |
| **Extensiones Python + Jupyter** | Complementos de VS Code | Permiten correr notebooks dentro de VS Code |
| **Librerías** (pandas, etc.) | "Fórmulas" adicionales de Python | Son las herramientas para manejar datos |

> 💡 **No usamos Anaconda.** Aunque es popular en ciencia de datos, su licencia
> exige pago para empresas grandes como Ford. Usamos el Python oficial, que es
> gratuito y sin restricciones.

---

## Paso 1 — Instalar Python

1. Entra a **https://www.python.org/downloads/**
2. Haz clic en el botón amarillo **"Download Python 3.x"** (la versión más reciente).
3. Abre el instalador que descargaste.
4. ⚠️ **MUY IMPORTANTE:** en la primera pantalla del instalador, **marca la casilla
   de abajo que dice "Add python.exe to PATH"** antes de continuar.

   ```
   ┌─────────────────────────────────────────────┐
   │  Install Python 3.x                         │
   │                                             │
   │   [ Install Now ]                           │
   │   [ Customize installation ]                │
   │                                             │
   │   ☑ Add python.exe to PATH   ← ¡MÁRCALA!    │
   └─────────────────────────────────────────────┘
   ```

5. Haz clic en **"Install Now"** y espera a que termine.
6. Cierra el instalador.

**Verificar que funcionó:** abre la aplicación **"Símbolo del sistema"** (busca
`cmd` en el menú de inicio) y escribe:

```cmd
python --version
```

Deberías ver algo como `Python 3.12.x`. Si dice que el comando no se reconoce,
ve a **Problemas comunes → "python no se reconoce"**.

---

## Paso 2 — Instalar Visual Studio Code (VS Code)

1. Entra a **https://code.visualstudio.com/**
2. Haz clic en **"Download for Windows"**.
3. Abre el instalador y sigue los pasos (puedes dejar todo por defecto).
   - 💡 Recomendado: marca la casilla **"Add to PATH"** si aparece.
4. Abre VS Code cuando termine.

---

## Paso 3 — Instalar las extensiones de VS Code

Las extensiones son complementos que le dan a VS Code la capacidad de abrir,
ver y ejecutar los notebooks.

Para instalar cada una: en la barra lateral izquierda haz clic en el ícono de
**Extensiones** (parecen 4 cuadritos, o presiona `Ctrl+Shift+X`), busca el
nombre o el **ID**, y haz clic en **Install**.

> 💡 **Atajo:** si abriste la carpeta del taller en VS Code, aparecerá una
> notificación abajo a la derecha que dice *"Do you want to install the
> recommended extensions?"* → haz clic en **Install** y se instalan las
> recomendadas de golpe.

### Esenciales (sin estas, los notebooks NO corren)

| Extensión | ID (para buscarla) | Para qué sirve |
|-----------|--------------------|----------------|
| **Python** | `ms-python.python` | El "motor". Ejecuta Python y detecta tu entorno `.venv`. |
| **Jupyter** | `ms-toolsai.jupyter` | Permite abrir y ejecutar los archivos `.ipynb`. |

Al instalar esas **dos**, VS Code descarga automáticamente sus componentes:
`Pylance` (autocompletado), `Python Debugger`, `Jupyter Keymap`,
**`Jupyter Notebook Renderers`** (dibuja las **gráficas** y las tablas),
`Jupyter Cell Tags` y `Jupyter Slide Show`. No necesitas instalarlos aparte.

### Recomendadas (opcionales, muy útiles en este curso)

| Extensión | ID | Por qué ayuda |
|-----------|-----|---------------|
| **Data Wrangler** | `ms-toolsai.datawrangler` | Ver los datos como una hoja de Excel, con filtros y estadísticas. |
| **Rainbow CSV** | `mechatroner.rainbow-csv` | Colorea las columnas de `ventas.csv` para leerlo fácil. |
| **Spanish Language Pack** | `ms-ceintl.vscode-language-pack-es` | Pone la interfaz de VS Code en español. |

Con las dos esenciales instaladas, VS Code ya puede abrir y ejecutar los
notebooks (`.ipynb`) del taller.

---

## Paso 4 — Descargar el material del taller

Si aún no lo has hecho, sigue las instrucciones de la sección **"Descargar
material"** del `README.md` (botón verde **Code → Download ZIP**, y descomprimir).

Luego, en VS Code: **Archivo → Abrir carpeta…** y selecciona la carpeta del
taller que descomprimiste (`python4FD2026`).

---

## Paso 5 — Crear el entorno e instalar las librerías

Un **entorno virtual** (`.venv`) es como una "caja" separada donde instalamos las
librerías del taller sin afectar el resto de tu computadora.

1. En VS Code abre la **Terminal**: menú **Terminal → New Terminal**
   (o `Ctrl+ñ`). Se abrirá una consola en la parte de abajo.

2. Crea el entorno virtual (escribe esto y presiona Enter):

   ```cmd
   python -m venv .venv
   ```

3. Actívalo:

   ```cmd
   .venv\Scripts\activate
   ```

   Sabrás que funcionó porque al inicio de la línea aparecerá `(.venv)`.

4. Instala las librerías del taller:

   ```cmd
   pip install -r requirements.txt
   ```

   Esto descarga pandas, matplotlib, duckdb y Jupyter. Puede tardar un par de
   minutos. Si falla por el proxy de Ford, ve a **Problemas comunes → proxy**.

---

## Paso 6 — Verificar que TODO quedó bien ✅

Este es el paso más importante. En la misma terminal (con `(.venv)` activo),
ejecuta el script de verificación:

```cmd
python modulo-0-instalacion/verificar_entorno.py
```

Si todo está bien, verás una lista de ✅ y el mensaje
**"¡Tu entorno está listo para el taller!"**.

Si algo sale con ✗, el script te dirá exactamente qué falta y cómo corregirlo.
Guarda una captura de pantalla del resultado por si necesitas ayuda en la sesión
de dudas.

---

## 🆘 Problemas comunes

### "python no se reconoce como comando..."
No marcaste **"Add python.exe to PATH"** al instalar. Solución más fácil:
vuelve a ejecutar el instalador de Python, elige **"Modify"** y activa la casilla
de PATH. Luego **cierra y vuelve a abrir** la terminal.

### `pip install` falla por el proxy / firewall de Ford
En redes corporativas, `pip` a veces no puede conectarse a internet. Prueba
indicándole el proxy de tu empresa (pídeselo a TI si no lo conoces):

```cmd
pip install --proxy http://usuario:contraseña@servidor-proxy:puerto -r requirements.txt
```

Ejemplo típico:

```cmd
pip install --proxy http://proxy.ford.com:83 -r requirements.txt
```

Si aun así falla, TI puede necesitar autorizar el acceso a `pypi.org`.

### "No tengo permisos de administrador" para instalar
Instalar Python o VS Code puede requerir permisos de administrador. Solicita a
**TI de Ford** que los instale o que te den permiso **antes** del taller. Al
instalar Python, la opción **"Install just for me"** (solo para mí) a veces evita
necesitar administrador.

### VS Code no encuentra el entorno `.venv`
Presiona `Ctrl+Shift+P`, escribe **"Python: Select Interpreter"** y elige el que
diga `.venv`. Así VS Code usa el entorno donde instalaste las librerías.

### El notebook pide "seleccionar kernel"
Al abrir un `.ipynb`, arriba a la derecha haz clic en **"Select Kernel"** y elige
el intérprete de `.venv` (o "Python Environments → .venv").

---

**¿Listo?** Si el Paso 6 te mostró todo en ✅, ya terminaste el pre-trabajo. 🎉
Nos vemos en el taller.

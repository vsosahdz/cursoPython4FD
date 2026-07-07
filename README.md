# 🚗 Python for Ford 2026 — Análisis de datos financieros

Taller práctico de **Python para finanzas y contabilidad**, nivel básico.
Aprenderás a cargar, explorar, analizar y graficar datos financieros con
**pandas**, **SQL (DuckDB)** y **matplotlib** — sin experiencia previa en
programación.

> 🌉 **La idea:** si sabes usar Excel (filtros, tablas dinámicas, BUSCARV), ya
> tienes la intuición. Aquí aprenderás a hacer lo mismo, pero con más potencia,
> usando código sencillo.

---

## 📥 Descargar el material

No necesitas saber usar `git`. Sigue estos pasos:

1. En la parte superior de esta página, haz clic en el botón verde **`< > Code`**.
2. En el menú que aparece, haz clic en **`Download ZIP`**.
3. Busca el archivo `.zip` en tu carpeta de **Descargas** y **descomprímelo**
   (clic derecho → *Extraer todo*).
4. Abre **VS Code** → menú **Archivo → Abrir carpeta…** → selecciona la carpeta
   `python4FD2026` que descomprimiste.

```
   Botón verde "Code"  ─►  "Download ZIP"  ─►  Descomprimir  ─►  Abrir en VS Code
```

> 💻 *(Opcional, solo si ya usas git):* `git clone <url-del-repo>`

---

## ⚙️ Instalación (Windows)

**Esto se hace ANTES del taller** (es el pre-trabajo). Toda la guía detallada,
paso a paso y con solución de problemas, está en:

👉 **[`modulo-0-instalacion/guia_instalacion.md`](modulo-0-instalacion/guia_instalacion.md)**

Resumen rápido:

1. Instala **Python** desde [python.org](https://www.python.org/downloads/)
   — ⚠️ marca la casilla **"Add python.exe to PATH"**.
2. Instala **VS Code** desde [code.visualstudio.com](https://code.visualstudio.com/).
3. En VS Code, instala las extensiones **Python** y **Jupyter** (de Microsoft).
4. Abre una terminal en VS Code (`Terminal → New Terminal`) y ejecuta:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. Verifica que todo quedó bien:
   ```cmd
   python modulo-0-instalacion/verificar_entorno.py
   ```
   Si ves todo en ✅, ¡estás listo! 🎉

> ℹ️ **No usamos Anaconda** (su licencia es de pago para empresas grandes).
> Usamos el Python oficial, gratuito.

---

## 🗂️ ¿Cómo está organizado?

```
python4FD2026/
├── datos/                     # El dataset del taller (ventas + concesionarios)
│   ├── generar_datos.py       #   script que crea los datos (reproducible)
│   ├── ventas.csv
│   └── concesionarios.csv
├── modulo-0-instalacion/      # PRE-TRABAJO: instalar herramientas
├── modulo-1-cargar-datos/     # Cargar y ver datos
├── modulo-2-tipos-datos/      # Tipos: categórico, numérico, fecha
├── modulo-3-filtrar-groupby/  # Filtrar y agrupar (tabla dinámica)
├── modulo-4-sql-duckdb/       # Consultas tipo SQL con DuckDB
├── modulo-5-visualizacion/    # Gráficas con matplotlib
├── proyecto-integrador/       # Caso final que junta todo
├── requirements.txt           # Librerías del taller
└── README.md                  # (este archivo)
```

Cada módulo (1 al 5) tiene:

| Archivo | ¿Qué es? | ¿Cuándo se usa? |
|---------|----------|-----------------|
| `guia.ipynb` | Explicación + ejemplos resueltos | Durante el taller en vivo |
| `reto.ipynb` | Ejercicios con autocomprobación (✅/✗) | **Después** de cada módulo, por tu cuenta |
| `soluciones.ipynb` | Respuestas de los retos | Se **liberan después** (ver abajo) |

---

## 📅 Ruta del taller

```
  1. PRE-TRABAJO          2. TALLER EN VIVO       3. RETOS              4. DUDAS
  ─────────────           ─────────────────       ──────────           ──────────
  Instalas las       →    4 horas guiadas    →    Resuelves el    →    2 horas de
  herramientas            (guia.ipynb de          reto.ipynb de        office hours
  (Módulo 0)              cada módulo)            cada módulo          para dudas
```

- **Pre-trabajo:** instala y verifica tu entorno (Módulo 0).
- **Taller en vivo (4 h):** recorremos juntos los `guia.ipynb` de los módulos 1–5.
- **Retos (asíncrono):** después de cada módulo resuelves su `reto.ipynb`. Cada
  ejercicio se **autocomprueba**: te dice al instante si acertaste (✅) o qué
  revisar (✗).
- **Sesión de dudas (2 h):** resolvemos juntos lo que se te haya atorado en los
  retos.

---

## 🔓 Sobre las soluciones

Las `soluciones.ipynb` **no están incluidas en la descarga inicial**, a
propósito: la idea es que primero intentes los retos por tu cuenta (la
autocomprobación te guía). Se publican **después** de la sesión de retos.

📄 Detalle de cómo y cuándo se liberan: [`SOLUCIONES.md`](SOLUCIONES.md).

---

## 🆘 Problemas comunes

| Problema | Solución rápida |
|----------|-----------------|
| `python` no se reconoce | No marcaste "Add to PATH" al instalar. Reinstala Python y marca la casilla. |
| `pip install` falla en la red de Ford | Es el proxy/firewall. Usa `pip install --proxy http://proxy.ford.com:83 -r requirements.txt` (pide el proxy a TI). |
| No tengo permisos de administrador | Pide a **TI de Ford** que instale Python y VS Code antes del taller. |
| El notebook pide "Select Kernel" | Elige el intérprete `.venv` (arriba a la derecha del notebook). |

Guía completa de solución de problemas en
[`modulo-0-instalacion/guia_instalacion.md`](modulo-0-instalacion/guia_instalacion.md).

---

*Material de capacitación interno. Datos 100% ficticios (no reales de Ford).*

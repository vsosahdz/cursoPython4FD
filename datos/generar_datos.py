"""
Generador del dataset dummy del taller "Python for Ford 2026".

Crea dos archivos CSV con datos FICTICIOS (no reales) de tema automotriz-financiero:

  - concesionarios.csv : catálogo de concesionarios (tabla dimensión, ~20 filas)
  - ventas.csv         : transacciones de venta (tabla de hechos, ~5,000 filas)

Los datos son deterministas (semilla fija), así que ejecutar este script siempre
produce exactamente los mismos archivos. Esto hace el material del taller reproducible.

Uso:
    python generar_datos.py

Requisitos: pandas (ver ../requirements.txt)
"""

import numpy as np
import pandas as pd

# Semilla fija -> datos reproducibles (mismos números en cada ejecución)
SEMILLA = 2026
rng = np.random.default_rng(SEMILLA)

N_VENTAS = 5000
FECHA_INICIO = "2024-01-01"
FECHA_FIN = "2025-12-31"

# ---------------------------------------------------------------------------
# 1) Catálogo de concesionarios (tabla dimensión)
# ---------------------------------------------------------------------------
concesionarios = pd.DataFrame(
    {
        "id_concesionario": range(1, 21),
        "nombre": [
            "Ford Monterrey Centro", "Ford San Nicolás", "Ford Saltillo",
            "Ford Torreón", "Ford CDMX Reforma", "Ford Satélite",
            "Ford Toluca", "Ford Querétaro", "Ford Puebla",
            "Ford Guadalajara Sur", "Ford Zapopan", "Ford León",
            "Ford Aguascalientes", "Ford Morelia", "Ford Mérida",
            "Ford Cancún", "Ford Veracruz", "Ford Villahermosa",
            "Ford Tuxtla", "Ford Oaxaca",
        ],
        "region": [
            "Norte", "Norte", "Norte", "Norte",
            "Centro", "Centro", "Centro", "Centro", "Centro",
            "Occidente", "Occidente", "Occidente", "Occidente", "Occidente",
            "Sureste", "Sureste", "Sureste", "Sureste", "Sureste", "Sureste",
        ],
        "ciudad": [
            "Monterrey", "San Nicolás", "Saltillo", "Torreón",
            "Ciudad de México", "Naucalpan", "Toluca", "Querétaro", "Puebla",
            "Guadalajara", "Zapopan", "León", "Aguascalientes", "Morelia",
            "Mérida", "Cancún", "Veracruz", "Villahermosa", "Tuxtla Gutiérrez",
            "Oaxaca",
        ],
        "gerente": [
            "Ana Torres", "Luis Guzmán", "María Peña", "Jorge Ríos",
            "Sofía Navarro", "Carlos Méndez", "Diana Flores", "Raúl Salas",
            "Patricia Lara", "Miguel Ángel Ruiz", "Laura Campos", "Héctor Vega",
            "Gabriela Ortiz", "Fernando Cano", "Rosa Aguilar", "Tomás Bravo",
            "Elena Ramos", "Óscar Domínguez", "Verónica Islas", "Andrés Cruz",
        ],
    }
)

# ---------------------------------------------------------------------------
# 2) Catálogo de modelos (precio y costo base por modelo, en MXN)
# ---------------------------------------------------------------------------
# categoria_vehiculo agrupa modelos; precio_base y costo_base dan realismo al margen.
modelos_info = {
    "Fiesta":   {"categoria": "Sedán",     "precio_base": 320_000,  "costo_base": 250_000},
    "Focus":    {"categoria": "Sedán",     "precio_base": 420_000,  "costo_base": 330_000},
    "Mustang":  {"categoria": "Deportivo", "precio_base": 1_250_000, "costo_base": 980_000},
    "F-150":    {"categoria": "Pickup",    "precio_base": 950_000,  "costo_base": 760_000},
    "Explorer": {"categoria": "SUV",       "precio_base": 1_050_000, "costo_base": 840_000},
    "Bronco":   {"categoria": "SUV",       "precio_base": 890_000,  "costo_base": 700_000},
}
modelos = list(modelos_info.keys())
# Algunos modelos se venden más que otros (pesos de probabilidad)
peso_modelos = np.array([0.22, 0.15, 0.08, 0.25, 0.18, 0.12])

metodos_pago = ["Contado", "Financiamiento", "Leasing"]
peso_metodos = np.array([0.35, 0.50, 0.15])

# ---------------------------------------------------------------------------
# 3) Transacciones de venta (tabla de hechos)
# ---------------------------------------------------------------------------
fechas_posibles = pd.date_range(FECHA_INICIO, FECHA_FIN, freq="D")
# Ligera estacionalidad: más ventas hacia fin de año
peso_fechas = 1.0 + 0.6 * np.sin(np.linspace(0, 3 * np.pi, len(fechas_posibles))) ** 2
peso_fechas = peso_fechas / peso_fechas.sum()

modelo_elegido = rng.choice(modelos, size=N_VENTAS, p=peso_modelos)
categoria = np.array([modelos_info[m]["categoria"] for m in modelo_elegido])
precio_base = np.array([modelos_info[m]["precio_base"] for m in modelo_elegido], dtype=float)
costo_base = np.array([modelos_info[m]["costo_base"] for m in modelo_elegido], dtype=float)

# Variación de precio (+/- 5%) y de costo (+/- 3%) por transacción
precio_unitario = np.round(precio_base * rng.normal(1.0, 0.05, N_VENTAS), -2)
costo_unitario = np.round(costo_base * rng.normal(1.0, 0.03, N_VENTAS), -2)

# La mayoría de las ventas son de 1 unidad; algunas ventas a flotillas de 2-5
unidades = rng.choice([1, 1, 1, 1, 2, 3, 4, 5], size=N_VENTAS)

# Descuento como porcentaje del precio (0% a 12%)
pct_descuento = rng.choice([0, 0, 0, 0.02, 0.03, 0.05, 0.08, 0.10, 0.12], size=N_VENTAS)
descuento = np.round(precio_unitario * unidades * pct_descuento, -1)

monto_venta = np.round(precio_unitario * unidades - descuento, -1)

ventas = pd.DataFrame(
    {
        "id_venta": range(1, N_VENTAS + 1),
        "fecha": rng.choice(fechas_posibles, size=N_VENTAS, p=peso_fechas),
        "id_concesionario": rng.integers(1, 21, size=N_VENTAS),
        "modelo": modelo_elegido,
        "categoria_vehiculo": categoria,
        "metodo_pago": rng.choice(metodos_pago, size=N_VENTAS, p=peso_metodos),
        "unidades": unidades,
        "precio_unitario": precio_unitario,
        "costo_unitario": costo_unitario,
        "descuento": descuento,
        "monto_venta": monto_venta,
    }
)

# Ordenar por fecha para que el CSV se vea natural
ventas = ventas.sort_values("fecha").reset_index(drop=True)
ventas["id_venta"] = range(1, N_VENTAS + 1)
# Formatear la fecha como texto YYYY-MM-DD (así los alumnos practican convertir a fecha)
ventas["fecha"] = pd.to_datetime(ventas["fecha"]).dt.strftime("%Y-%m-%d")

# ---------------------------------------------------------------------------
# 4) Guardar a CSV
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import os

    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_conc = os.path.join(carpeta, "concesionarios.csv")
    ruta_ventas = os.path.join(carpeta, "ventas.csv")

    concesionarios.to_csv(ruta_conc, index=False, encoding="utf-8")
    ventas.to_csv(ruta_ventas, index=False, encoding="utf-8")

    print("✅ Datos generados correctamente:")
    print(f"   - {ruta_conc}  ({len(concesionarios)} filas)")
    print(f"   - {ruta_ventas}  ({len(ventas)} filas)")
    print()
    print("Vista previa de ventas.csv:")
    print(ventas.head())

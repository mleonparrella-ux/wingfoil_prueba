# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:20:23 2026

@author: usuario
"""

from src.carga_datos import cargar_dataset, limpiar_datos
from src.visualizaciones import grafico_sensacion_promedio, grafico_wings

df = cargar_dataset()

if df is None:
    exit()

df = limpiar_datos(df)

print("\n====================")
print(" DASHBOARD WINGFOIL ")
print("====================")

print(
    "\nTotal sesiones:",
    len(df)
)

print(
    "Viento promedio:",
    round(
        df["Vel. Viento (kn)"].mean(),
        2
    )
)

print(
    "Sensación promedio:",
    round(
        df["Sensación"].mean(),
        2
    )
)

while True:

    print("\n===== DASHBOARD =====")

    print("1 - Uso de Wings")
    print("2 - Sensación por Wing")
    print("0 - Salir")

    opcion = input(
        "Seleccione una opción: "
    )

    if opcion == "1":

        grafico_wings(df)

    elif opcion == "2":

        grafico_sensacion_promedio(df)

    elif opcion == "0":

        break

    else:

        print(
            "Opción inválida"
        )
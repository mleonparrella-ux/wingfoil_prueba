# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:19:35 2026

@author: usuario
"""

from src.carga_datos import cargar_dataset, limpiar_datos
from src.validaciones import validar_viento
from src.analisis_datos import mostrar_metricas
from src.recomendaciones import recomendar_wing

df = cargar_dataset()

if df is None:
    exit()

df = limpiar_datos(df)

while True:

    print("\n===== WINGFOIL =====")

    print("1 - Ver métricas")
    print("2 - Recomendar Wing")
    print("0 - Salir")

    opcion = input(
        "Seleccione una opción: "
    )

    if opcion == "1":

        mostrar_metricas(df)

    elif opcion == "2":

        viento = input(
            "Ingrese intensidad del viento (en Knt): "
        )
        ubicacion = input("Ingrese ubicacion: "
        ) 
        direccion = input("Ingrese direccion: "
                          )
        if validar_viento(viento):

            recomendar_wing(
                df,
                ubicacion,
                float(viento),
                direccion
            )

        else:

            print(
                "Viento inválido"
            )

    elif opcion == "0":

        print("Fin del programa")

        break

    else:

        print(
            "Opción inválida"
        )
        

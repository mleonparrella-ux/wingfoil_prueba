# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:19:35 2026
@author: usuario
MAIN.PY - Interfaz de Lógica y Registro
"""
from src.carga_datos import cargar_dataset, limpiar_datos, registrar_sesion
from src.validaciones import validar_viento
from src.analisis_datos import mostrar_metricas
from src.recomendaciones import recomendar_wing
import sys 

df = cargar_dataset()
if df is None:
    sys.exit() 

df = limpiar_datos(df)

while True:
    print("\n===== WINGFOIL =====")
    print("1 - Ver métricas")
    print("2 - Recomendar Wing")
    print("3 - Registrar sesión nueva")
    print("0 - Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        mostrar_metricas(df)

    elif opcion == "2":
        viento = input("Ingrese intensidad del viento (en Knt): ").strip()
        ubicacion = input("Ingrese ubicacion: ").strip() 
        direccion = input("Ingrese direccion: ").strip()
        
        if validar_viento(viento):
            recomendar_wing(df, ubicacion, float(viento), direccion)
        else:
            print("Viento inválido")
   
    elif opcion == "3":
        print("\n=== REGISTRAR SESIÓN NUEVA ===")
        ubicacion = input("Ingresa una ubicacion: ")
        vel_viento = input("Ingresa la velocidad del viento en Knt: ")
        dir_viento = input("Ingresa la direccion del viento: ")
        wing = input("Ingresa el wing: ")
        tabla = input("Ingresa la tabla: ")
        foil = input("Ingresa el foil: ")
        sensacion = input("Ingresa la sensacion: ")
        
       
        
        nueva_sesion_dict = {
            "Ubicación": ubicacion,
            "Vel. Viento (kn)": vel_viento,
            "Dirección Viento": dir_viento,
            "Wing": wing,
            "Tabla": tabla,
            "Foil": foil,
            "Sensación": sensacion
        }
        
        df = registrar_sesion(df, nueva_sesion_dict)
        print("\n¡Sesión guardada de manera persistente!")

    elif opcion == "0":
        print("Fin del programa")
        break
    else:
        print("Opción inválida")
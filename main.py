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
import src.appi_clima as appi_clima

API_KEY = "TU_API_KEY"

df = cargar_dataset()
if df is None:
    exit()

df = limpiar_datos(df)

while True:
    print("\n===== WINGFOIL =====")
    print("1 - Ver métricas")
    print("2 - Recomendar Wing")
    print("3 - Registrar sesión nueva (Con API)")
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
        ubicacion_input = input("¿Dónde navegaste hoy? (Ciudad): ").strip()
        condicion_agua = input("Condición del agua (flat/chop moderado): ").strip()
        
        viento_vel = None
        viento_dir = None
        
        try:
            print("Consultando clima en tiempo real...")
            datos_json = appi_clima.consultar_clima(ubicacion_input, API_KEY)
            viento_vel, viento_dir = appi_clima.procesar_datos_viento(datos_json)
            print(f"-> Viento obtenido por API: {viento_vel} kn | Dirección: {viento_dir}°")
        except Exception:
            print("\n[Aviso]: Falló la API. Activando ingreso manual.")
            viento_vel = input("Velocidad del viento manual (kn): ").strip()
            while not validar_viento(viento_vel):
                print("[Error]: Intensidad inválida.")
                viento_vel = input("Ingrese una velocidad válida (kn): ").strip()
            viento_vel = float(viento_vel)
            viento_dir = int(input("Dirección del viento en grados (0-360): "))

        print("\n--- Detalles del Equipamiento ---")
        wing = input("Wing utilizada: ").strip()
        tabla = input("Tabla utilizada: ").strip()
        foil = input("Foil utilizado: ").strip()
        sensacion = int(input("Sensación de la sesión (1-10): "))
        
        nueva_sesion_dict = {
            "Ubicación": ubicacion_input,
            "Condición Agua": condicion_agua,
            "Vel. Viento (kn)": viento_vel,
            "Dirección Viento": viento_dir,
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
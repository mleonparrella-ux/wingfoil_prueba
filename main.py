from src.validaciones import validar_viento, validar_sensacion, validar_duracion
from src.carga_datos import cargar_dataset, limpiar_datos, registrar_sesion
from src.analisis_datos import mostrar_metricas
from src.recomendaciones import recomendar_wing
import src.api_clima as api_clima

import sys 


API_KEY = "830c4fe781f2bcf133755085f9cdbf22" 

df = cargar_dataset()
if df is None:
    sys.exit() 

df = limpiar_datos(df)

while True:
    print("\n=WINGFOIL =")
    print("1 - Ver métricas")
    print("2 - Recomendar Wing")
    print("3 - Registrar sesión nueva")
    print("0 - Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        try:
            mostrar_metricas(df)
        except Exception as e:
            print(f"[ERROR CRÍTICO]: No se pudieron mostrar las métricas. {e}")

    elif opcion == "2":
        try:
            ubicacion = input("Ingrese ubicacion: ").strip()
            viento = input("Ingrese intensidad del viento (en kn): ").strip()
            print("Direcciones válidas: Norte, Sur, Este, Oeste, Noreste, Sudeste, Noroeste, Sudoeste")
            direccion = input("Ingrese direccion del viento: ").strip()
            if validar_viento(viento):
                recomendar_wing(df, ubicacion, float(viento), direccion)
            else:
                print("Viento inválido.")
        except Exception as e:
            print(f"[ERROR CRÍTICO]: Error al generar recomendación. {e}")

    elif opcion == "3":
        print("\n=== REGISTRAR SESIÓN NUEVA ===")
        ubicacion_input = input("¿Dónde navegaste hoy? : ").strip()
        fecha = input("Ingresa una fecha (AAAA-MM-DD): ")
        duracion = input("Ingresa la duracion en minutos: ")
        wing = input("Ingresa el wing (en m): ")
        tabla = input("Ingresa la tabla (en litros): ")
        foil = input("Ingresa el foil : ")
        sensacion = input("Ingresa la sensacion: ")
        viento_vel = None
        viento_dir = None
        try:
            print("Consultando clima en tiempo real...")
            datos_json = api_clima.consultar_clima(ubicacion_input, API_KEY)
            viento_vel, viento_dir = api_clima.procesar_datos_viento(datos_json)
            print(f"-> Viento obtenido por API: {viento_vel} kn | Dirección: {viento_dir}")
        except Exception as e:
            print(e)
            print("\n[Aviso]: Falló la API. Activando ingreso manual.")
            ubicacion_input = input("Ingresa una ubicacion: ")
            fecha = input("Ingresa una fecha (AAAA-MM-DD): ")
            duracion = input("Ingresa la duracion en minutos: ")
            viento_vel = input("Ingresa la velocidad del viento en kn: ")
            viento_dir = input("Ingresa la direccion del viento: ")
            wing = input("Ingresa el wing (en m): ")
            tabla = input("Ingresa la tabla (en litros): ")
            foil = input("Ingresa el foil: ")
            sensacion = input("Ingresa la sensacion: ")
            while not validar_viento(viento_vel):
                print("[Error]: Intensidad inválida.")
                viento_vel = input("Ingrese una velocidad válida (kn): ").strip()
            viento_vel = float(viento_vel)
        try:
            nueva_sesion_dict = {
                "Fecha": fecha,
                "Ubicación": ubicacion_input,
                "Duración (min)": int(duracion),
                "Vel. Viento (kn)": viento_vel,
                "Dir. Viento": viento_dir,
                "Wing": wing,
                "Tabla": tabla,
                "Foil": foil,
                "Sensación": int(sensacion)
            }
            df = registrar_sesion(df, nueva_sesion_dict)
            print("\n¡Sesión guardada de manera persistente!")
        except Exception as e:
            print(f"[ERROR CRÍTICO]: No se pudo guardar la sesión. {e}")

    elif opcion == "0":
        print("Fin del programa")
        break
    else:
        print("Opción inválida")

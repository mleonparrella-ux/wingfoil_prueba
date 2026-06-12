# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:40 2026

@author: usuario
"""

import pandas as pd

# UNIFICADO: Ruta correcta para leer y escribir siempre en el mismo archivo
ARCHIVO = "datos/dataset_sesiones.xlsx"

def cargar_dataset():

    try:

        df = pd.read_excel(
            ARCHIVO
        )

        return df

    except Exception as e:

        print("Error al cargar dataset")
        print(e)

        return None


def verificar_columnas(df):

    # CORREGIDO: Cambiado "Dir. Viento" por "Dirección Viento" para que calce 
    # perfectamente con los datos que procesa la API y lo que espera el DataFrame
    columnas = [
        "Fecha",
        "Ubicación",
        "Duración (min)",
        "Vel. Viento (kn)",
        "Dirección Viento",
        "Wing",
        "Tabla",
        "Foil",
        "Sensación"
    ]

    for columna in columnas:

        if columna not in df.columns:

            print(
                f"Falta la columna {columna}"
            )

            return False

    return True


def limpiar_datos(df):

    df = df.dropna()

    return df


def registrar_sesion(df_actual, datos_nuevos):
    """
    Registra una nueva sesión sumándola al DataFrame actual y
    guardando el resultado en el archivo de Excel de forma segura.
    """
    try:
        # 1. Convertimos el diccionario recibido en una fila de Pandas
        nueva_fila = pd.DataFrame([datos_nuevos])
        
        # 2. Concatenamos la nueva fila al DataFrame actual
        df_actualizado = pd.concat([df_actual, nueva_fila], ignore_index=True)
        
        # 3. Guardamos en el Excel de forma persistente en la ruta unificada
        df_actualizado.to_excel(ARCHIVO, index=False)
        
        return df_actualizado
        
    except Exception as e:
        print(f"\n[Error al guardar]: No se pudo escribir en el archivo Excel. {e}")
        return df_actual
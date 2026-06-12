# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:40 2026

@author: usuario
"""

import pandas as pd

ARCHIVO = "dataset_sesiones.xlsx"

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

    columnas = [
        "Fecha",
        "Ubicación",
        "Duración (min)",
        "Vel. Viento (kn)",
        "Dir. Viento",
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
    ruta_excel = "datos/dataset_sesiones.xlsx"
    
    try:
        # 1. Convertimos el diccionario con los datos en una fila de Pandas
        nueva_fila = pd.DataFrame([datos_nuevos])
        
        # 2. Sumamos la nueva fila al historial usando concat (la forma limpia de Pandas)
        df_actualizado = pd.concat([df_actual, nueva_fila], ignore_index=True)
        
        # 3. Guardamos el Excel actualizado sin índices duplicados
        df_actualizado.to_excel(ruta_excel, index=False)
        
        return df_actualizado
        
    except Exception as e:
        print(f"\n[Error al guardar]: No se pudo escribir en el archivo Excel. {e}")
        return df_actual

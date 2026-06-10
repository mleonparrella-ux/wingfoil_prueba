# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:40 2026

@author: usuario
"""

import pandas as pd


def cargar_dataset():

    try:

        df = pd.read_excel(
            "data/dataset_sesiones.xlsx"
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

def registrar_sesion(df, archivo_excel):
    """
    Registra una nueva sesión y la guarda en el dataset.
    """

    nueva_sesion = {
        "Fecha": input("Fecha (AAAA-MM-DD): "),
        "Ubicación": input("Ubicación: "),
        "Duración (min)": int(input("Duración (min): ")),
        "Vel. Viento (kn)": float(input("Velocidad del viento (kn): ")),
        "Dir. Viento": input("Dirección del viento: "),
        "Wing": input("Wing utilizada: "),
        "Tabla": input("Tabla utilizada: "),
        "Foil": float(input("Foil utilizado: ")),
        "Sensación": int(input("Sensación (1-10): "))
    }

    # Agregar al DataFrame
    df = pd.concat(
        [df, pd.DataFrame([nueva_sesion])],
        ignore_index=True
    )

    # Guardar cambios
    df.to_excel(archivo_excel, index=False)

    print("Sesión registrada correctamente.")

    return df

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

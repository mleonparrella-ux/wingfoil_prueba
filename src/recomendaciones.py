# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:42 2026
@author: usuario
"""
import pandas as pd



def buscar_sesiones_similares(df, ubicacion, viento, direccion):
    """
    Busca sesiones similares por ubicación, dirección y viento (±3 kn).
    Args: df (DataFrame), ubicacion (str), viento (float), direccion (str)
    Returns: DataFrame con las sesiones similares.
    """
    df = df.copy()
    df["Vel. Viento (kn)"] = pd.to_numeric(df["Vel. Viento (kn)"], errors="coerce")
    df = df.dropna(subset=["Vel. Viento (kn)"])
    similares = df[
        (df["Ubicación"].str.lower() == ubicacion.lower())
        &
        (df["Dir. Viento"].str.lower() == direccion.lower())
        &
        (abs(df["Vel. Viento (kn)"] - viento) <= 3)
        ]
    return similares

def recomendar_wing(df, ubicacion, viento, direccion):
    """
    Recomienda el wing con mejor sensación promedio en sesiones similares.
    Args: df (DataFrame), ubicacion (str), viento (float), direccion (str)
    """
    similares = buscar_sesiones_similares(df, ubicacion, viento, direccion)
    if len(similares) == 0:
        print("\nNo se encontraron sesiones similares.")
        return
    if len(similares) < 3:
        print(f"\nAtención: solo se encontraron {len(similares)} sesiones similares.")
    promedio_por_wing = (
        similares
        .groupby("Wing")["Sensación"]
        .mean()
        .sort_values(ascending=False)
    )
    wing_recomendado = promedio_por_wing.index[0]
    print("\n===== RECOMENDACIÓN =====")
    print("Wing recomendado:", wing_recomendado)
    print("Sensación esperada:", round(promedio_por_wing.iloc[0], 2))
    print("Basado en", len(similares), "sesiones similares")
    return wing_recomendado
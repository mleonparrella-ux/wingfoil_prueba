# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:42 2026

@author: usuario
"""

def buscar_sesiones_similares(
        df,
        ubicacion,
        viento,
        direccion
):

    similares = df[
        (df["Ubicación"] == ubicacion)
        &
        (df["Dir. Viento"] == direccion)
        &
        (
            abs(
                df["Vel. Viento (kn)"]
                - viento
            ) <= 3
        )
        

    return similares


def recomendar_wing(
        df,
        ubicacion,
        viento,
        direccion
):

    similares = buscar_sesiones_similares(
        df,
        ubicacion,
        viento,
        direccion
    )

    if len(similares) == 0:

        print(
            "No hay sesiones similares."
        )

        return

    if len(similares) < 3:

        print(
            f"Advertencia: solo se encontraron {len(similares)} sesiones similares."
        )

    promedio_por_wing = (
        similares
        .groupby("Wing")["Sensación"]
        .mean()
    )

    wing_recomendado = (
        promedio_por_wing.idxmax()
    )

    print("\n===== RECOMENDACIÓN =====")

    print(
        "Wing recomendado:",
        wing_recomendado
    )

    print(
        "Sensación promedio esperada:",
        round(
            promedio_por_wing.max(),
            2
        )
    )

    print(
        "Basado en",
        len(similares),
        "sesiones similares"
    )

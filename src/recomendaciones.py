# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:42 2026

@author: usuario
"""

def buscar_sesiones_similares(
        df,
        ubicacion,
        viento,
        sensacion
):

    similares = df[
        (df["Ubicación"] == ubicacion)
        &
        (
            abs(
                df["Vel. Viento (kn)"]
                - viento
            ) <= 3
        )
        &
        (
            abs(
                df["Sensación"]
                - sensacion
            ) <= 1
        )
    ]

    return similares


def recomendar_wing(
        df,
        ubicacion,
        viento,
        sensacion
):

    similares = buscar_sesiones_similares(
        df,
        ubicacion,
        viento,
        sensacion
    )

    if len(similares) == 0:

        print(
            "\nNo se encontraron sesiones similares."
        )

        return

    promedio_por_wing = (
        similares
        .groupby("Wing")["Sensación"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    wing_recomendado = (
        promedio_por_wing.index[0]
    )

    print("\n===== RECOMENDACIÓN =====")

    print(
        "Wing recomendado:",
        wing_recomendado
    )

    print(
        "Sensación esperada:",
        round(
            promedio_por_wing.iloc[0],
            2
        )
    )

    print(
        "Basado en",
        len(similares),
        "sesiones similares"
    )

    return wing_recomendado
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:42 2026

@author: usuario
"""

def buscar_sesiones_similares(
        df,
        viento
):

    similares = df[
        abs(
            df["Vel. Viento (kn)"]
            - viento
        ) <= 3
    ]

    return similares


def recomendar_wing(
        df,
        viento
):

    similares = buscar_sesiones_similares(
        df,
        viento
    )

    if len(similares) == 0:

        print(
            "No hay sesiones similares."
        )

        return

    wing = (
        similares["Wing"]
        .mode()[0]
    )

    print("\nWing recomendado:")

    print(wing)

    print(
        "Basado en",
        len(similares),
        "sesiones similares"
    )

    print(
        "Sensación promedio:",
        round(
            similares["Sensación"].mean(),
            2
        )
    )
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:42 2026

@author: usuario
"""

def mostrar_metricas(df):

    print("\n===== MÉTRICAS =====")

    print(
        "Cantidad de sesiones:",
        len(df)
    )

    print(
        "Viento promedio:",
        round(
            df["Vel. Viento (kn)"].mean(),
            2
        )
    )

    print(
        "Sensación promedio:",
        round(
            df["Sensación"].mean(),
            2
        )
    )

    print(
        "Ubicaciones distintas:",
        df["Ubicación"].nunique()
    )
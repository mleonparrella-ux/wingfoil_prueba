# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:54:20 2026

@author: usuario
"""

def mostrar_resumen(df):

    print("\n===== RESUMEN =====")

    print(
        "Total de sesiones:",
        len(df)
    )

    print(
        "Sensación promedio:",
        round(
            df["Sensación"].mean(),
            2
        )
    )
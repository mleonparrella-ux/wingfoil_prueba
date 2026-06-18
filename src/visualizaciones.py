# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:44 2026

@author: usuario
"""

import matplotlib.pyplot as plt

def grafico_wings(df):
    """
    Muestra un gráfico de barras con la cantidad de usos de cada wing.
    """

    wings = df["Wing"].value_counts()

    colores = [
        "royalblue",
        "orange",
        "green",
        "red",
        "purple",
        "gold",
        "cyan"
    ]

    plt.figure(figsize=(8, 5))

    wings.plot(
        kind="bar",
        color=colores[:len(wings)]
    )

    plt.title("Cantidad de sesiones por Wing")
    plt.xlabel("Wing")
    plt.ylabel("Cantidad de sesiones")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()
    
def grafico_sensaciones(df):
    """
    Muestra la distribución de las sensaciones en un gráfico de torta.
    """

    sensaciones = (
        df["Sensación"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(7, 7))

    plt.pie(
        sensaciones,
        labels=sensaciones.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Distribución de Sensaciones")

    plt.show()
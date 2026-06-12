# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:44 2026

@author: usuario
"""

import matplotlib.pyplot as plt

def grafico_wings(df):

    datos = (
        df["Wing"]
        .value_counts()
    )

    plt.figure(figsize=(8,5))

    plt.bar(
        datos.index,
        datos.values
    )

    plt.title(
        "Uso de Wings"
    )

    plt.show()


def grafico_sensacion_promedio(df):

    datos = (
        df.groupby("Wing")
        ["Sensación"]
        .mean()
    )

    plt.figure(figsize=(8,5))

    plt.bar(
        datos.index,
        datos.values
    )

    plt.title(
        "Sensación promedio por Wing"
    )

    plt.ylabel(
        "Sensación"
    )

    plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:12:41 2026

@author: usuario
"""

def validar_viento(viento):

    try:

        viento = float(viento)

        return viento > 0

    except:

        return False


def validar_opcion(opcion):

    opciones = [
        "1",
        "2",
        "3",
        "4",
        "0"
    ]

    return opcion in opciones
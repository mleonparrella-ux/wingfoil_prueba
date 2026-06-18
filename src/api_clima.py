# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:35:23 2026
@author: usuario
"""
# -- coding: utf-8 --
"""
Created on Fri Jun  5 12:12:45 2026
@author: usuario
API_CLIMA.PY - Módulo Meteorológico Adaptado a Consigna de Cátedra (Blindado)
Este archivo NO maneja interacción con el usuario (no tiene print ni input).
"""
import requests

def validar_ubicacion(ubicacion):
    """Valida que la ubicación ingresada sea un texto válido."""
    if not ubicacion or not isinstance(ubicacion, str) or ubicacion.strip() == "":
        raise ValueError("La ubicación no puede estar vacía y debe ser un texto válido.")

def consultar_clima(ubicacion, api_key):
    """
    Consulta la API de OpenWeatherMap usando parámetros estructurados.
    Si hay un error en la respuesta o conexión, eleva un error con 'raise'.
    """
    validar_ubicacion(ubicacion)
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": ubicacion,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        respuesta = requests.get(url, params=params, timeout=5)
    except requests.exceptions.RequestException:
        raise ConnectionError("No se pudo establecer conexión con el servidor de clima.")
        
    if respuesta.status_code == 404:
        raise NameError(f"La ubicación '{ubicacion}' no fue encontrada en el servicio meteorológico.")
    elif respuesta.status_code != 200:
        raise RuntimeError(f"Error inesperado de la API. Código de estado: {respuesta.status_code}")
        
    return respuesta.json()

def grados_a_cardinal(grados):
    """Convierte grados (0-360) a punto cardinal."""
    puntos = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"]
    indice = round(grados / 45) % 8
    return puntos[indice]

def procesar_datos_viento(datos_json):
    """
    Extrae la velocidad y dirección del viento.
    Realiza la conversión matemática de metros por segundo a nudos.
    Convierte la dirección de grados a punto cardinal.
    """
    if 'wind' not in datos_json:
        raise KeyError("La respuesta recibida no contiene datos meteorológicos de viento.")
        
    viento_ms = datos_json['wind']['speed']
    viento_nudos = round(viento_ms * 1.94384, 1)
    
    grados = datos_json['wind'].get('deg', 0)
    viento_direccion = grados_a_cardinal(grados)
    
    return viento_nudos, viento_direccion
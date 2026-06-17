def mostrar_metricas(df):
    """
    Muestra métricas generales del historial de sesiones.
    Args: df (DataFrame): historial de sesiones.
    """
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
    print(
        "Días navegados:",
        df["Fecha"].nunique()
    )
    # CORREGIDO: Se agregó el paréntesis de cierre que faltaba al final del round
    print(
        "Duración promedio:",
        round(
            df["Duración (min)"].mean(),
            2
        )
    )

def mostrar_resumen(df):
    """
    Muestra un resumen rápido del historial de sesiones.
    Args: df (DataFrame): historial de sesiones.
    """
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

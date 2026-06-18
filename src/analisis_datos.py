def mostrar_resumen(df):

    print("\n===== RESUMEN GENERAL =====")

    print(
        "Total de sesiones:",
        len(df)
    )

    print(
        "Periodo registrado:",
        df["Fecha"].min(),
        "->",
        df["Fecha"].max()
    )

    print(
        "Ubicaciones visitadas:",
        df["Ubicación"].nunique()
    )

    print(
        "Horas totales navegadas:",
        round(
            df["Duración (min)"].sum() / 60,
            2
        ),
        "hs"
    )

    print(
        "Duración total:",
        df["Duración (min)"].sum(),
        "min"
    )

    print(
        "Viento promedio:",
        round(
            df["Vel. Viento (kn)"].mean(),
            2
        ),
        "kn"
    )

    print(
        "Sensación promedio:",
        round(
            df["Sensación"].mean(),
            2
        )
    )

    print(
        "Wing más utilizado:",
        df["Wing"].mode()[0]
    )


def mostrar_metricas(df):

    print("\n===== MÉTRICAS DETALLADAS =====")

    print(
        "Cantidad de sesiones:",
        len(df)
    )

    print(
        "Duración promedio:",
        round(
            df["Duración (min)"].mean(),
            2
        ),
        "min"
    )

    print(
        "Duración máxima:",
        df["Duración (min)"].max(),
        "min"
    )

    print(
        "Viento mínimo:",
        df["Vel. Viento (kn)"].min(),
        "kn"
    )

    print(
        "Viento máximo:",
        df["Vel. Viento (kn)"].max(),
        "kn"
    )

    print(
        "Viento promedio:",
        round(
            df["Vel. Viento (kn)"].mean(),
            2
        ),
        "kn"
    )

    print(
        "Sensación promedio:",
        round(
            df["Sensación"].mean(),
            2
        )
    )

    print(
        "Mejor sensación:",
        df["Sensación"].max()
    )

    print(
        "Ubicación favorita:",
        df["Ubicación"].mode()[0]
    )

    print(
        "Wing favorito:",
        df["Wing"].mode()[0]
    )

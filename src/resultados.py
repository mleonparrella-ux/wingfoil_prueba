
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

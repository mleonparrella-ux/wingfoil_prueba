import pandas as pd
# UNIFICADO: Ruta correcta para leer y escribir siempre en el mismo archivo
ARCHIVO = "data/dataset_sesiones.xlsx"

def cargar_dataset():
    try:
        df = pd.read_excel(
            ARCHIVO
        )
        return df
    except Exception as e:
        print("Error al cargar dataset")
        print(e)
        return None

def verificar_columnas(df):
    columnas = [
        "Fecha",
        "Ubicación",
        "Duración (min)",
        "Vel. Viento (kn)",
        "Dir. Viento",
        "Wing",
        "Tabla",
        "Foil",
        "Sensación"
    ]
    for columna in columnas:
        if columna not in df.columns:
            print(
                f"Falta la columna {columna}"
            )
            return False
    return True

def limpiar_datos(df):
    df = df.dropna()
    df["Vel. Viento (kn)"] = pd.to_numeric(df["Vel. Viento (kn)"], errors="coerce")
    df["Sensación"] = pd.to_numeric(df["Sensación"], errors="coerce")
    df["Duración (min)"] = pd.to_numeric(df["Duración (min)"], errors="coerce")
    df = df.dropna()
    return df

def registrar_sesion(df_actual, datos_nuevos):
    """
    Registra una nueva sesión sumándola al DataFrame actual y
    guardando el resultado en el archivo de Excel de forma segura.
    """
    try:
        nueva_fila = pd.DataFrame([datos_nuevos])
        df_actualizado = pd.concat([df_actual, nueva_fila], ignore_index=True)
        df_actualizado.to_excel(ARCHIVO, index=False)
        return df_actualizado
    except Exception as e:
        print(f"\n[Error al guardar]: No se pudo escribir en el archivo Excel. {e}")
        return df_actual
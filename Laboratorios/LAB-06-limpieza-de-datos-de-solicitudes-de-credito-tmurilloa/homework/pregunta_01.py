"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
from pathlib import Path
import pandas as pd


def limpiar_texto(col: pd.Series, strip: bool = True) -> pd.Series:
    """
    Limpia una columna de texto:
    - Minúsculas
    - Reemplaza espacios, puntos y guiones por guiones bajos
    - Opcionalmente elimina espacios alrededor
    """
    col = col.str.lower().str.replace(r"[ .-]", "_", regex=True)
    return col.str.strip() if strip else col


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza limpieza general del DataFrame:
    - Elimina filas con datos faltantes
    - Estandariza columnas de texto y categorías
    - Convierte montos a float, fechas y categorías
    """
    df = df.dropna().copy()

    # Limpieza y conversión de monto
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.removeprefix("$ ")
        .str.replace(",", "")
        .astype(float)
    )

    # Columnas de texto que deben estandarizarse y convertirse a categoría
    columnas_categoria = [
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]
    for col in columnas_categoria:
        df[col] = limpiar_texto(df[col], strip=(col != "barrio")).astype("category")

    # Normalización de sexo
    df["sexo"] = df["sexo"].str.lower().astype("category")

    # Conversión de tipos
    df["estrato"] = df["estrato"].astype("category")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int).astype("category")
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], dayfirst=True, format="mixed"
    )

    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    return df


def pregunta_01():
    """
    Limpia el archivo 'solicitudes_de_credito.csv' eliminando:
    - Duplicados
    - Registros nulos
    - Texto inconsistente
    Guarda el resultado en 'files/output/solicitudes_de_credito.csv'
    """
    # Leer datos
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

    # Aplicar limpieza
    df_limpio = limpiar_datos(df)

    # Guardar resultado
    out_path = Path("files/output")
    out_path.mkdir(parents=True, exist_ok=True)
    df_limpio.to_csv(out_path / "solicitudes_de_credito.csv", sep=";")
    

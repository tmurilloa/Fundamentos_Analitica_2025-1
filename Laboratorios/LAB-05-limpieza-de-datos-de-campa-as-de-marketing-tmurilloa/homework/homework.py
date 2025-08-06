"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel
import glob
import zipfile
import pandas as pd
import os

def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """
    ruta_carpeta = "files/input"
    archivos_zip = glob.glob(f"{ruta_carpeta}/*.zip")

    dataframes = []

    print("Zips encontrados:", archivos_zip)

    for archivo_zip in archivos_zip:
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            nombres = zip_ref.namelist()[0]
            
            with zip_ref.open(nombres) as f:
                df = pd.read_csv(f, index_col=None)
                dataframes.append(df)

    df_combinado = pd.concat(dataframes, ignore_index=True)

    # ---- DF Cliente -------
    columnas_cliente = ["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]
    df_cliente = df_combinado[columnas_cliente].copy()

    # columna job
    df_cliente["job"] = df_cliente["job"].str.replace(".", "", regex=False)
    df_cliente["job"] = df_cliente["job"].str.replace("-", "_", regex=False)

    # columna education
    df_cliente["education"] = df_cliente["education"].str.replace(".", "_", regex=False)
    df_cliente["education"] = df_cliente["education"].replace("unknown", pd.NA)

    # Columna credit_default y mortgage
    df_cliente["credit_default"] = df_cliente["credit_default"].apply(lambda x: 1 if str(x).lower() == "yes" else 0)

    df_cliente["mortgage"] = df_cliente["mortgage"].apply(lambda x: 1 if str(x).lower() == "yes" else 0)

    # ----- DF campaign -------
    columnas_campaign = ["client_id","number_contacts","contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]

    meses = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12"
    }


    df_campaign = df_combinado[columnas_campaign].copy()

    # Columna previous_outcome
    df_campaign["previous_outcome"] = df_campaign["previous_outcome"].apply(lambda x: 1 if str(x).lower() == "success" else 0)

    # Columna campaign outcome
    df_campaign["campaign_outcome"] = df_campaign["campaign_outcome"].apply(lambda x: 1 if str(x).lower() == "yes" else 0)

    # Columna last_contact_day
    df_campaign["last_contact_date"] = "2022" + "-" +df_combinado["month"].str.lower().map(meses)+ "-" + df_combinado["day"].astype(str)


    # ------ DF economics ------
    columnas_economics = ["client_id", "cons_price_idx", "euribor_three_months"]

    df_economics = df_combinado[columnas_economics].copy()

    os.makedirs("files/output", exist_ok=True)
    df_cliente.to_csv("files/output/client.csv", index=False)
    df_campaign.to_csv("files/output/campaign.csv", index= False)
    df_economics.to_csv("files/output/economics.csv", index=False)

    



if __name__ == "__main__":
   clean_campaign_data()

"""Taller evaluable presencial"""

#
# Este codigo impolementa algoritmo 'fingerprint' para colision de textos, el
# cual es utilizado para unificar cadenas de texto que representan la misma
# entidad.
#
# Referencia:
# https://openrefine.org/docs/technical-reference/clustering-in-depth
#
import nltk  # type: ignore
import pandas as pd  # type: ignore


def load_data(input_file):
    """Lea el archivo usando pandas y devuelva un DataFrame"""

    df = pd.read_csv(input_file)
    return df


def create_normalized_key(df):
    """Cree una nueva columna en el DataFrame que contenga
    el key de la columna 'raw_text'"""

    df = df.copy()

    # Copie la columna 'text' a la columna 'key'
    df["key"] = df["raw_text"]

    # Remueva los espacios en blanco al principio y al final de la cadena
    df["key"] = df["key"].str.strip()

    # Convierta el texto a minúsculas
    df["key"] = df["key"].str.lower()

    # Transforme palabras que pueden (o no) contener guiones por su
    # version sin guion (este paso es redundante por la linea siguiente.
    # Pero es claro anotar la existencia de palabras con y sin '-'.
    df["key"] = df["key"].str.replace("-", "")

    # Remueva puntuación y caracteres de control
    df["key"] = df["key"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    )

    # Convierta el texto a una lista de tokens
    df["key"] = df["key"].str.split()

    # Transforme cada palabra con un stemmer de Porter
    stemmer = nltk.PorterStemmer()
    df["key"] = df["key"].apply(lambda x: [stemmer.stem(word) for word in x])

    # Ordene la lista de tokens y remueve duplicados
    df["key"] = df["key"].apply(lambda x: sorted(set(x)))

    # Convierta la lista de tokens a una cadena de texto separada por espacios
    df["key"] = df["key"].str.join(" ")

    return df

def generate_cleaned_text(df):
    """Crea la columna 'cleaned_text' en el DataFrame"""

    keys = df.copy()

    # Ordene el dataframe por 'key' y 'text'
    keys = keys.sort_values(by=["key", "raw_text"], ascending=[True, True])

    # Seleccione la primera fila de cada grupo de 'key'
    keys = df.drop_duplicates(subset="key", keep="first")

    # Cree un diccionario con 'key' como clave y 'text' como valor
    key_dict = dict(zip(keys["key"], keys["raw_text"]))

    # Cree la columna 'cleaned' usando el diccionario
    df["cleaned_text"] = df["key"].map(key_dict)

    return df


def save_data(df, output_file):
    """Guarda el DataFrame en un archivo"""

    df = df.copy()
    df = df[["raw_text", "cleaned_text"]]
    df.to_csv(output_file, index=False)

def main(input_file, output_file):
    """Ejecuta la limpieza de datos"""

    df = load_data(input_file)
    df = create_normalized_key(df)
    df = generate_cleaned_text(df)
    df.to_csv("files/test.csv", index=False)
    save_data(df, output_file)

    print(df)


if __name__ == "__main__":
    main(
        input_file="files/input.txt",
        output_file="files/output.txt",
    )

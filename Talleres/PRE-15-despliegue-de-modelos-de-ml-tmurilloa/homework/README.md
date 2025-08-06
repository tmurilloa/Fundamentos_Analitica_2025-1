# Descripción

Este taller presencial tiene como objetivo demostra el proceso de construcción y 
despliegue de modelos de machine learning.

**Parte 1**.--- Entrene un modelo de machine learning en scikit-learn que permita 
pronosticar el precio de una casa a partir de sus propiedades. La data
para el entrenamiento del modelo se encuenctra en el archivo `house_data.csv`. 
El modelo usa las columnas 

* "bedrooms",
  
* "bathrooms",
  
* "sqft_living",

* "sqft_lot",

* "floors",

* "waterfront",

* "condition".

El archivo con el código para entrenamiento del modelo debe llamarse 
`train_model.py`. Ejemplifique el uso del modelo desde el terminal usando
curl.


**Parte 2**.--- En el archivo `api_server.py` escriba el código para desplegar 
un servicio API que retorna el pronóstico del precio para una casa.

**Parte 3**.--- En el archivo `api_client.py`  escriba un programa en Python
que consulte el servicio API escrito en la Parte 2.

**Parte 4**.--- En el archivo `web_app.py`  escriba el código para desplegar
una aplicación de Flask que permita al usuario ingresar valores y que
retorne el precio de la casa

![house-predictor](https://github.com/jdvelasq/PRE_sklearn_despliegue_de_modelos/main/house_predictor.png)


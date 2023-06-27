from config.config import Config
import requests
from openai_completion import obtener_resumenes_noticias
from actualTime import obtener_hora_actual

print(obtener_hora_actual())

api_key = Config.MEDIASTACK.API_KEY

def getNewsUrls(topic):
    url = "http://api.mediastack.com/v1/news"
    # Parámetros de la solicitud
    params = {
        "access_key": api_key,
        "keywords": topic,
        "countries": "ar",
        "limit": 10,
        "sort": "published_desc"
    }

    # Realizar la solicitud GET con el encabezado de autorización
    response = requests.get(url, headers={"Authorization": "Bearer " + api_key}, params=params)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Procesar la respuesta JSON
        data = response.json()
        # Hacer algo con los datos obtenidos
            # Iterar sobre las descripciones de las noticias
        print(response.json())
    
        return data['data']
    else:
        # Mostrar el código de estado en caso de error
        print("Error:", response.status_code)

print(getNewsUrls('elecciones'))
import pymongo
import sys
from flask import Flask, request, jsonify
from config.config import Config
from flask_pymongo import ObjectId
from flask_cors import CORS
import requests

try:
  client = pymongo.MongoClient(Config.MONGO.MONGO_URI)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

db=client.newsdb


# FLASK CONFIGURATION
app=Flask(__name__)
CORS(app)
api_key = Config.MEDIASTACK.API_KEY

# use a collection named "recipes"
news = db["news"]

# Crear el índice de texto antes de definir la función postNewsByKeyword
news.create_index([('author', 'text'), ('title', 'text'), ('description', 'text'), ('source', 'text')], default_language='none')

# ----------------------------------- POST DE NOTICIAS GENERALES -----------------------------------
@app.route('/', methods=['POST'])
def postNews():
    url = "http://api.mediastack.com/v1/news"
    # Parámetros de la solicitud
    params = {
        "access_key": api_key,
        "limit": 100,
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
        for data in data['data']:
           
            if data['image'] is not None:
                existing_news = news.find_one({
                    'title': data['title'],
                    'source': data['source']
                })

                if existing_news is None:
                    result = news.insert_one({
                        'author': data['author'],
                        'title': data['title'],
                        'description': data['description'],
                        'url': data['url'],
                        'source': data['source'],
                        'image': data['image'],
                        'category': data['category'],
                        'language': data['language'],
                        'country': data['country'],
                        'published_at': data['published_at'],
                    })
                    inserted_id = str(result.inserted_id)
                else:
                    inserted_id = str(existing_news['_id'])


        return jsonify(inserted_id)
        
    else:
        # Mostrar el código de estado en caso de error
        print("Error:", response.status_code)

# ----------------------------------- POST DE NOTICIAS ARGENTINAS -----------------------------------
@app.route('/news/ar', methods=['POST'])
def postArgNews():
    url = "http://api.mediastack.com/v1/news"
    # Parámetros de la solicitud
    params = {
        "access_key": api_key,
        "countries": "ar",
        "limit": 100,
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
        for data in data['data']:
            if data['image'] is not None:
                existing_news = news.find_one({
                    'title': data['title'],
                    'source': data['source']
                })

                if existing_news is None:
                    result = news.insert_one({
                        'author': data['author'],
                        'title': data['title'],
                        'description': data['description'],
                        'url': data['url'],
                        'source': data['source'],
                        'image': data['image'],
                        'category': data['category'],
                        'language': data['language'],
                        'country': data['country'],
                        'published_at': data['published_at'],
                    })
                    inserted_id = str(result.inserted_id)
                else:
                    inserted_id = str(existing_news['_id'])

        return jsonify(inserted_id)
        
    else:
        # Mostrar el código de estado en caso de error
        print("Error:", response.status_code)


# ----------------------------------- POST DE NOTICIAS DE TECNOLOGIA -----------------------------------
@app.route('/news/technology', methods=['POST'])
def postTechNews():
    url = "http://api.mediastack.com/v1/news"
    # Parámetros de la solicitud
    params = {
        "access_key": api_key,
        "categories": "technology",
        "languages": "es",
        "limit": 100,
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
        for data in data['data']:
            if data['image'] is not None:
                existing_news = news.find_one({
                    'title': data['title'],
                    'source': data['source']
                })

                if existing_news is None:
                    result = news.insert_one({
                        'author': data['author'],
                        'title': data['title'],
                        'description': data['description'],
                        'url': data['url'],
                        'source': data['source'],
                        'image': data['image'],
                        'category': data['category'],
                        'language': data['language'],
                        'country': data['country'],
                        'published_at': data['published_at'],
                    })
                    inserted_id = str(result.inserted_id)
                else:
                    inserted_id = str(existing_news['_id'])

        return jsonify(inserted_id)
        
    else:
        # Mostrar el código de estado en caso de error
        print("Error:", response.status_code)


# FUNCION PARA TRAER DE LA API NOTICIAS EN BASE A UNA PALABRA ESPECIFICA

# @app.route('/news/<keyword>', methods=['POST'])
# def postNewsByKeyword(keyword):
#     url = "http://api.mediastack.com/v1/news"
#     # Parámetros de la solicitud
#     params = {
#         "access_key": api_key,
#         "keywords": keyword,
#         "limit": 10,
#         "sort": "published_desc"
#     }

#     # Realizar la solicitud GET con el encabezado de autorización
#     response = requests.get(url, headers={"Authorization": "Bearer " + api_key}, params=params)

#     # Verificar el código de estado de la respuesta
#     if response.status_code == 200:
#         # Procesar la respuesta JSON
#         data = response.json()
#         # Hacer algo con los datos obtenidos
#         # Iterar sobre las descripciones de las noticias
#         for data in data['data']:
#             if data['image'] is not None:
#                 existing_news = news.find_one({
#                     'title': data['title'],
#                     'source': data['source']
#                 })

#                 if existing_news is None:
#                     result = news.insert_one({
#                         'author': data['author'],
#                         'title': data['title'],
#                         'description': data['description'],
#                         'url': data['url'],
#                         'source': data['source'],
#                         'image': data['image'],
#                         'category': data['category'],
#                         'language': data['language'],
#                         'country': data['country'],
#                         'published_at': data['published_at'],
#                     })
#                     inserted_id = str(result.inserted_id)
#                 else:
#                     inserted_id = str(existing_news['_id'])

#         return jsonify(inserted_id)
#     else:
#         # Mostrar el código de estado en caso de error
#         print("Error:", response.status_code)

# ----------------------------------- GET DE BUSQUEDA -----------------------------------
@app.route('/news/search', methods=['GET'])
def getNewsByKeyword():
    keyword = request.args.get('keyword')  # Obtener la palabra clave desde los parámetros de consulta

    news_list = []
    cursor = news.find({'$text': {'$search': keyword}})

    for doc in cursor:
        news_list.append({
            '_id': str(ObjectId(doc['_id'])),
            'author': doc['author'],
            'title': doc['title'],
            'description': doc['description'],
            'url': doc['url'],
            'source': doc['source'],
            'image': doc['image'],
            'category': doc['category'],
            'language': doc['language'],
            'country': doc['country'],
            'published_at': doc['published_at']
        })

    return jsonify(news_list)


# ----------------------------------- GET DE TODAS LA NOTICIAS -----------------------------------

@app.route('/', methods=['GET'])
def getNews():
    news_list = []
    for doc in news.find():
        news_list.append({
            '_id': str(ObjectId(doc['_id'])),
            'author': (doc['author']),
            'title': (doc['title']),
            'description':(doc['description']),
            'url': (doc['url']),
            'source': (doc['source']),
            'image': (doc['image']),
            'category': (doc['category']),
            'language': (doc['language']),
            'country': (doc['country']),
            'published_at': (doc['published_at']),
        })
    return jsonify(news_list)


# ----------------------------------- GET DE NOTICIAS ARGENTINAS -----------------------------------
@app.route('/news/ar', methods=['GET'])
def getArgNews():
    news_list = []
    for doc in news.find():
        if doc['country'] == 'ar':
            news_list.append({
                '_id': str(ObjectId(doc['_id'])),
                'author': (doc['author']),
                'title': (doc['title']),
                'description':(doc['description']),
                'url': (doc['url']),
                'source': (doc['source']),
                'image': (doc['image']),
                'category': (doc['category']),
                'language': (doc['language']),
                'country': (doc['country']),
                'published_at': (doc['published_at']),
            })
    return jsonify(news_list)

# ----------------------------------- GET DE NOTICIAS DE TECNOLOGIA -----------------------------------
@app.route('/news/technology', methods=['GET'])
def getTechNews():
    news_list = []
    for doc in news.find():
        if doc['category'] == 'technology':
            news_list.append({
                '_id': str(ObjectId(doc['_id'])),
                'author': (doc['author']),
                'title': (doc['title']),
                'description':(doc['description']),
                'url': (doc['url']),
                'source': (doc['source']),
                'image': (doc['image']),
                'category': (doc['category']),
                'language': (doc['language']),
                'country': (doc['country']),
                'published_at': (doc['published_at']),
            })
    return jsonify(news_list)

# ----------------------------------- GET ONE NEWS -----------------------------------
@app.route('/news/<string:id>', methods=['GET'])
def getOneNews(id):
    one_news = news.find_one({'_id': ObjectId(id)})
    if one_news is not None:
        one_news['_id'] = str(one_news['_id'])
        return jsonify(one_news)
    else:
        return jsonify({'message': 'Noticia no encontrada'}), 404




if __name__ == "__main__":
    app.run(debug=True, port=4000)
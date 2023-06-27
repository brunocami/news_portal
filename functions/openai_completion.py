import openai
from config.config import Config

def obtener_resumenes_noticias(data):
    # Establecer tus credenciales de API de OpenAI
    openai.api_key = Config.OPENAI.OPENAI_API_KEY

    resumenes = []
    # Obtener resumen para cada URL
    for url in data:
        # Generar resumen utilizando la API de OpenAI
        respuesta = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Haz un resumen mediantemente extenso, ni muy corto ni muy largo pero que no se escapen los detalles importantes, y en el idioma en que fue escrita la noticia en la siguiente URL: {url}\n",
            temperature= 0.7,
            max_tokens= 300,
            top_p= 1,
            frequency_penalty= 0.2,
            presence_penalty= 0.8,
            n= 1,
            stop= "<STOP>",
        )
        resumen = respuesta.choices[0].text.strip()
        resumenes.append(resumen)

    return resumenes



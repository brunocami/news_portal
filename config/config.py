# Configuraciones generales
class MediastackConfig:
    API_KEY='485e912e0b893b9a50bbad8862751035'

class MongoUri: 
    MONGO_URI='mongodb+srv://newsportaldb:<password>@news.u7dacnl.mongodb.net/?retryWrites=true&w=majority'
    SECRET_KEY="8X3R2D7Z6A1B0C9H5K4"

class OpenAiConfig:
    OPENAI_API_KEY='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'

# Configuración global
class Config:
    MEDIASTACK=MediastackConfig
    OPENAI= OpenAiConfig
    MONGO=MongoUri
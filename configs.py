from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','20972373'))
    API_HASH = getenv('API_HASH','dd79a3c317054edbd63f75fd6e918bd1')
    BOT_TOKEN = getenv('BOT_TOKEN','6948717739:AAF7gD8OfBKgzOTb_BDsntpN1YrYaSu0JJo')

config = Config()

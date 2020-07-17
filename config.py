import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SIMILAR_URL = 'https://api.themoviedb.org/3/movie/{}/similar?api_key={}'
    GENRES_URL ='https://api.themoviedb.org/3/genre/movie/list?api_key={}'
    GENRE_MOVIES_URL = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres={}'
    COLLECTION_URL = 'https://api.themoviedb.org/3/collection/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_LIFE = True
    SIMPLEMDE_USE_CDN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cwilv:iamcwilv@localhost/watchlist_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cwilv:iamcwilv@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
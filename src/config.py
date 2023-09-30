from decouple import config

app_debug = config('APP_DEBUG', default='')
app_debug = app_debug.strip().lower()
app_debug = app_debug == 'true'

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = app_debug

config = {
    'development': DevelopmentConfig,
    'host': config('APP_HOST', default='0.0.0.0'),
    'port': config('APP_PORT', default='5000')
}
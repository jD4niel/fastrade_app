class Config:
    SECRET_KEY = 'Qaracolito23129023ikdm'

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
}
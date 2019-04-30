import os

class Config:
  '''
  General configuration parent class
  '''
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY ='fefe'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
      Config:The parent configuration class with General configuration settings

  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://faithrehema:fefe@localhost/pitch'
  # SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
      Config: The parent configuration class with general configuration settings 

  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://faithrehema:fefe@localhost/pitch'
  

  DEBUG = True 

class TestConfig(Config):
  '''
This is the class which we will use to set the configurations during testing stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties

  '''
config_options ={
    'development':DevConfig,
    'production': ProdConfig,
    'test':TestConfig
  }

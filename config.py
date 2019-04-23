import os
class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY ='fefe'
class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
      Config:The parent configuration class with General configuration settings

  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
      Config: The parent configuration class with general configuration settings 

  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://faithrehema:shalomneema@locolhost/pitch'
  

  DEBUG = True 

config_options ={
    'development':DevConfig,
    'production': ProdConfig
  }

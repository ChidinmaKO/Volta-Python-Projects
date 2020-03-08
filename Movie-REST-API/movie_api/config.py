import os


class Config:
    ''' Set Flask configuration variables '''
    
    # general
    SECRET_KEY = 'yadayadayada'
    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

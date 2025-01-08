import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/tc_python_framework'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://root:ZSYIcH1QS1n19PU5Y3J3JwcRQgJwQuhE@dpg-ctv1uhtds78s738m7leg-a.oregon-postgres.render.com:5432/qap_framework_database_ieai'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSWORD_HASH_SALT = "tc#123456"

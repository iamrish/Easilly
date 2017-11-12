import os

# default config

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x17?le\x9c.\xa5y\xaf@\xda0Y\xfa\xeb(\x97\t\xae\x8a\x02\x96\xa6'

	# jab databse bhi decide na ho ki konse environment me konsa dena hai!
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False 	 
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	FLASKY_MAIL_SUBJECT_PREFIX = '[Rainbow]'
	FLASKY_MAIL_SENDER = 'Rainbow Admin <showeryhe@hotmail.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUT = True
	MAIL_SERVER = 'smtp-mail.outlook.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('showeryhe')
	MAIL_PASSWORD = os.environ.get('hxo@1009')
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://CommonLanguage:19870408@localhost/service'
	# os.environ.get('DEV_DATABASE_URL') or
	#	'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test@localhost/test'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://CommonLanguage:19870408@localhost/service'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
}

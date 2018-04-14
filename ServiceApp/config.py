import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or '<secret>'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	FLASKY_MAIL_SUBJECT_PREFIX = '<secret>'
	FLASKY_MAIL_SENDER = '<secret> <<secret>@hotmail.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUT = True
	MAIL_SERVER = 'smtp-mail.outlook.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('<secret>')
	MAIL_PASSWORD = os.environ.get('<secret>')
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<secret>:<secret>@localhost/<secret>'
	# os.environ.get('DEV_DATABASE_URL') or
	#	'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<secret>:<secret>@localhost/<secret>'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<secret>:<secret>@localhost/<secret>'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
}

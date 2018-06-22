#-*- coding:utf-8 -*-

from flask import Flask, render_template, json, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField, SelectField, SelectMultipleField, IntegerField, SelectMultipleField, FormField, SubmitField
from wtforms.validators import Required, AnyOf
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from werkzeug import generate_password_hash, check_password_hash
from flask_script import Shell
from flask_moment import Moment
from config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	
	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	
	return app

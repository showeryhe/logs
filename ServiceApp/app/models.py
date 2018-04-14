#-*- coding:utf-8 -*-

from flask import Flask, render_template, json, request, session, redirect, url_for, jsonify
# from datatables import ColumnDT, DataTables
# import MySQLdb
from flask_bootstrap import Bootstrap
# import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from flask_script import Shell, Manager
from datetime import datetime
from wtforms_sqlalchemy.orm import model_form


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://CommonLanguage:19870408@localhost/service'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role, Service=Service)

manager=Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='role')

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	service = db.relationship('Service', backref='handler')

class Service(db.Model):
	__tablename__ = 'service'
	id = db.Column(db.Integer, primary_key=True)
	service_cate = db.Column(db.String(64), nullable=False, index=True)
#	date = db.Column(db.String(16), nullable=False, index=True)
#	handler = db.Column(db.String(64), nullable=False, index=True)
#	channel = db.Column(db.String(64), nullable=False, index=True)
#	case_cate = db.Column(db.String(64), nullable=False, index=True)
#	brief = db.Column(db.String(64), nullable=False)
#	notes = db.Column(db.String(64), nullable=True)
#	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	# ForeignKey
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




#-*- coding:utf-8 -*-
from flask import Flask, render_template, json, request, session, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Shell, Manager
from datetime import datetime
from flask_login import UserMixin
import itsdangerous, flask_mail 
from . import login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://CommonLanguage:19870408@localhost/service'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Role(db.Model):
	__tablename__ = 'roles_1'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	# BackRef
	users = db.relationship('User', backref='role')

class User(db.Model):
	__tablename__ = 'users_1'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	# ForeignKey
	role_id = db.Column(db.Integer, db.ForeignKey('roles_1.id'))
	# BackRef
	lcc = db.relationship('LegalCaseConsult', backref='handler')
	lc = db.relationship('LegalConsult', backref='handler')
	def is_authenticated(self):
		return True
	def get_id(self):
		return unicode(self.id)
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

class LegalCasePerson(db.Model):
	__tablename__ = 'lcp_3'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	sex = db.Column(db.String(64))
	gender_identity = db.Column(db.String(64))
	sexual_orientation = db.Column(db.String(64))
	age = db.Column(db.String(64))
	contact_info = db.Column(db.String(64))
	recourse_means = db.Column(db.String(64))
	location = db.Column(db.String(64))
	economic_status = db.Column(db.String(64))
	case_category = db.Column(db.String(64))
	marriage_status= db.Column(db.Boolean)
	case_brief = db.Column(db.String(64))
	legal_needs = db.Column(db.String(64))
	previous_recourse = db.Column(db.String(64))
	post_script = db.Column(db.String(64))
	date = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)
	# Back Ref
	consult = db.relationship('LegalCaseConsult', backref='lcp')
	# Foreign Key
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	
class LegalCaseConsult(db.Model):
	__tablename__ = 'lcc_3'
	lcc_id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(64))
	consult_brief = db.Column(db.String(64))
	following_up = db.Column(db.String(64))
	post_script = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)
	# Foreign Key
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	person_id = db.Column(db.Integer, db.ForeignKey('lcp_3.id'))

class LegalConsult(db.Model):
	__tablename__ = 'lc_3'
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(64))
	name = db.Column(db.String(64))
	sex = db.Column(db.String(64))
	gender_identity = db.Column(db.String(64))
	sexual_orientation = db.Column(db.String(64))
	age = db.Column(db.String(64))
	location = db.Column(db.String(64))
	recourse_method = db.Column(db.String(64))
	consult_category = db.Column(db.String(64))
	marriage_status = db.Column(db.Boolean)
	recourse_means = db.Column(db.String(64))
	consult_brief = db.Column(db.Text(128))
	consult_answer = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)	
	# ForeignKey
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))

class AntiCaseStart(db.Model):
	__tablename__ = 'acs_3'
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.String(64))
	recourse_source = db.Column(db.String(64))
	recourse_method = db.Column(db.String(64))
	multi_cooperation = db.Column(db.String(64))
	service_method = db.Column(db.String(64))
	case_brief = db.Column(db.String(64))
	name = db.Column(db.String(64))
	sex = db.Column(db.String(64))
	gender_identity = db.Column(db.String(64))
	sexual_orientation = db.Column(db.String(64))
	age = db.Column(db.String(64))
	contact_info = db.Column(db.String(64))
	location = db.Column(db.String(64))
	job_status = db.Column(db.Boolean)
	job_description = db.Column(db.String(64))
	family_description = db.Column(db.String(64))
	education = db.Column(db.String(64))
	economic_status = db.Column(db.String(64))
	relation_status = db.Column(db.String(64))
	relation_lasting =db.Column(db.String(64))
	living_status = db.Column(db.String(64))
	risk = db.Column(db.String(64))
	other_info = db.Column(db.String(64))
	anti_role = db.Column(db.String(64))
	relation = db.Column(db.String(64))
	case_category = db.Column(db.String(64))
	violent_category = db.Column(db.String(64))
	violent_category_spirit = db.Column(db.String(64))
	violent_category_spirit_other = db.Column(db.String(64))
	violent_category_strain = db.Column(db.String(64))
	violent_category_other = db.Column(db.String(64))
	communication_control = db.Column(db.String(64))
	brief = db.Column(db.String(64))
	injury = db.Column(db.String(64))
	recourse_others = db.Column(db.String(64))
	advocate_suggestions = db.Column(db.String(64))
	requirement = db.Column(db.String(64))
	requirement_analysis = db.Column(db.String(64))
	service_goal = db.Column(db.String(64))
	cooperation_requirement = db.Column(db.String(64))
	resources = db.Column(db.String(64))
	social_relation_1 = db.Column(db.String(64))
	social_support_1 = db.Column(db.String(64))
	social_relation_2 = db.Column(db.String(64))
	social_support_2 = db.Column(db.String(64))
	social_relation_3 = db.Column(db.String(64))
	social_support_3 = db.Column(db.String(64))
	first_service = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)
	#Back Ref
	consult = db.relationship('AntiCaseConsult', backref='acs')
	ending = db.relationship('AntiCaseEnding', backref='ace')
	# Foreign Key
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	
class AntiCaseConsult(db.Model):
	__tablename__ = 'acc_2'
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(64))
	service = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)
	# Foreign Key
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	person_id = db.Column(db.Integer, db.ForeignKey('acs_3.id'))	
	
class AntiCaseEnding(db.Model):
	__tablename__ = 'ace_2'
	id = db.Column(db.Integer, primary_key=True)
	conclusion_status = db.Column(db.String(64))
	conclusion = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime, default = datetime.utcnow)	
	# Foreign Key
	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	person_id = db.Column(db.Integer, db.ForeignKey('acs_3.id'))

#class AntiConsult(db.Model):
#	__tablename__ = 'ac_1'
#	id = db.Column(db.Integer, primary_key=True)
#	timestamp = db.Column(db.DateTime, default = datetime.utcnow)
#	# Foreign Key	
#	handler_id = db.Column(db.Integer, db.ForeignKey('users_1.id'))
	
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



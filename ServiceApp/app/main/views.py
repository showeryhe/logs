#-*- coding:utf-8 -*-

from flask import Flask, render_template, json, request, session, redirect, url_for
from datetime import datetime
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
from . import main
from .forms import NameForm, ServiceForm
from .. import db
from ..models import User, Service
import sqlalchemy_json
from sqlalchemy.orm import class_mapper

def serialize(model):
	columns = [c.key for c in class_mapper(model.__class__).columns]
	return dict((c, getattr(model, c)) for c in columns)
@main.route('/data')
def data():
	test = [[s.id, s.service_cate, User.query.filter_by(id=s.user_id).first().username] for s in Service.query.all()]
#	serialize(label)
#	for label in Service.query.all()]
	jtest = json.dumps(test)
#在/ServiceApp下生成文件
#	with open('./app/templates/data_2.txt', 'w') as f:
#		f.write('{"data":')
#		f.write(json.dumps(test))
#		f.write('}')
#	return render_template('data.html')	
#	for t in test:
#		jtest.append(json.dump(t))
	return render_template('data.html', jtest=jtest)

@main.route('/log', methods=['GET','POST'])
def log():
	form = ServiceForm()
	form.handler.choices = [(u.id, u.username) for u in User.query.all()]
	if form.validate_on_submit():
#		handler = User.query.filter_by(username=handler_name).first()
#		if handler is None:
#			return redirect(url_for('log'))
#		else:
		service = Service(
			service_cate = form.service_cate.data,
#				date = form.date.data,
#				handler = form.handler.data,
#				channel = form.channel.data,
#				case_cate = form.case_cate.data,
#				brief = form.brief.data,
#				notes = form.notes.data,
			user_id = form.handler.data)
		db.session.add(service)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form)

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('main.index'))
	return render_template('index.html',
		form = form, name = session.get('name'),
		known = session.get('known', False))

@main.route('/user/<name>')
def user(user):
	return render_template('user.html', name = name)

@main.route('/lookUp')
def lookUp():
	return render_template('lookup.html')

@main.route('/chat')
def chat():
	form=ServiceForm()
	return render_template('log.html', form=form)

@main.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@main.route('/signUp', methods = ['POST', 'GET'])
def signUp():
	try:
		_name = request.form['inputName']
		_password = request.form['inputPassword']
	
		if _name and _password:
			conn = mysql.connect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('user', (_name, _hased_password))
			data = cursor.fetchall()
			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'Congratulations!'})
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html': '<span>Emmmm...</span>'})
	except Exception as e:
		return json.dumps({'error': str(e)})
	finally:
		cursor.close()
		conn.close()

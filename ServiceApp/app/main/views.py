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
from .forms import NameForm, LegalCasePersonForm, LegalCaseConsultForm, LegalConsultForm, AntiCaseStartForm, AntiCaseDocForm, AntiCasePersonForm, AntiCaseServiceForm, AntiCaseConsultForm, AntiCaseEndingForm, AntiCaseStartDataForm, AntiCaseEndingDataForm
from .. import db
from ..models import User, LegalCasePerson, LegalCaseConsult, LegalConsult, AntiCaseStart, AntiCaseConsult, AntiCaseEnding#, AntiConsult
import sqlalchemy_json
from sqlalchemy.orm import class_mapper
from flask_login import login_required, current_user

#=============查询=============
@main.route('/data', methods=['GET', 'POST'])
@login_required
def data():
	return render_template('data.html', funcname = 'data')

@main.route('/data/legal_case_person', methods=['GET','POST'])
@login_required
def data_legal_case_person():
	category = u'法律个案 - 案主档案'
	lcp = [[s.name, s.sex, s.gender_identity, s.sexual_orientation, s.age, s.contact_info, s.recourse_means, s.location, s.economic_status, s.case_category, s.marriage_status, s.case_brief, s.legal_needs, s.previous_recourse, s.post_script, s.date, User.query.filter_by(id=s.handler_id).first().username, "<a href=legal_case_consult_"+str(s.id)+">查看</a>"] for s in LegalCasePerson.query.all()]
	lcps = json.dumps(lcp)
	return render_template('data.html', jtest=lcps, category=category, cate = 1)

@main.route('/data/legal_case_consult_<id>', methods=['GET','POST'])
@login_required
def data_legal_case_consult_individual(id):
	name = LegalCasePerson.query.get_or_404(id).name
	category = u'法律个案 - ' + name + u'服务记录'
	consults = LegalCaseConsult.query.filter_by(person_id = id)
	lcc = [[s.date, s.consult_brief, s.following_up, s.post_script, User.query.get_or_404(s.handler_id).username] for s in consults]
	lccs = json.dumps(lcc)
	return render_template('data.html', jtest=lccs, category=category, cate = 3)	
	
@main.route('/data/legal_consult', methods=['GET','POST'])
@login_required
def data_legal_consult():
	category = u'法律咨询'
	lc = [[s.date, s.name, s.sex, s.gender_identity, s.sexual_orientation, s.age, s.location, s.recourse_method, s.consult_category, s.marriage_status, s.recourse_means, s.consult_brief, s.consult_answer, User.query.filter_by(id=s.handler_id).first().username] for s in LegalConsult.query.all()]
	lcs = json.dumps(lc)
	return render_template('data.html', jtest = lcs, category=category, cate = 4)

@main.route('/data/anti_case_start', methods=['GET','POST'])
@login_required
def data_anti_case_start():
	category = u'反家暴个案 - 案主档案'
	acs= [[s.time, s.name, s.case_category, s.case_brief, User.query.filter_by(id=s.handler_id).first().username,
	"<a href = anti_case_start_"+ str(s.id) + ">查看</a>",
	"<a href = anti_case_consult_"+ str(s.id) + ">查看</a>",
	"<a href = anti_case_ending_" + str(s.id) + ">查看</a>"] for s in AntiCaseStart.query.all()]
	acss = json.dumps(acs)
	return render_template('data.html', jtest=acss, category=category, cate = 5)

@main.route('/data/anti_case_start_<id>', methods=['GET','POST'])
@login_required
def data_anti_case_start_individual(id):
	ACS = AntiCaseStart.query.get_or_404(id)
	category = u'个案 - ' + ACS.name + u'服务记录'
	form = AntiCaseStartDataForm()
	if form.validate_on_submit():
		return render_template('log_success.html')
	form.time.data = ACS.time
	form.recourse_source.data = ACS.recourse_source
	form.recourse_method.data = ACS.recourse_method
	form.multi_cooperation.data = ACS.multi_cooperation
	form.service_method.data = ACS.service_method
	form.case_brief.data = ACS.case_brief
	form.name.data = ACS.name
	form.sex.data = ACS.sex
	form.gender_identity.data = ACS.gender_identity
	form.sexual_orientation.data = ACS.sexual_orientation
	form.age.data = ACS.age
	form.contact_info.data = ACS.contact_info
	form.location.data = ACS.location
	form.job_status.data = ACS.job_status
	form.job_description.data = ACS.job_description
	form.family_description.data = ACS.family_description
	form.education.data = ACS.education
	form.economic_status.data = ACS.economic_status
	form.relation_status.data = ACS.relation_status
	form.relation_lasting.data = ACS.relation_lasting
	form.living_status.data = ACS.living_status
	form.risk.data = ACS.risk
	form.other_info.data = ACS.other_info
	form.anti_role.data = ACS.anti_role
	form.relation.data = ACS.relation
	form.case_category.data = ACS.case_category
	form.violent_category.data = ACS.violent_category
	form.violent_category_spirit.data = ACS.violent_category_spirit
	form.violent_category_spirit_other.data = ACS.violent_category_spirit_other
	form.violent_category_strain.data = ACS.violent_category_strain
	form.violent_category_other.data = ACS.violent_category_other
	form.communication_control.data = ACS.communication_control
	form.brief.data = ACS.brief
	form.injury.data = ACS.injury
	form.recourse_others.data = ACS.recourse_others
	form.advocate_suggestions.data = ACS.advocate_suggestions
	form.requirement.data = ACS.requirement
	form.requirement_analysis.data = ACS.requirement_analysis
	form.service_goal.data = ACS.service_goal
	form.cooperation_requirement.data = ACS.cooperation_requirement
	form.resources.data = ACS.resources
	form.social_relation_1.data = ACS.social_relation_1
	form.social_support_1.data = ACS.social_support_1
	form.social_relation_2.data = ACS.social_relation_2
	form.social_support_2.data = ACS.social_support_2
	form.social_relation_3.data = ACS.social_relation_3
	form.social_support_3.data = ACS.social_support_3
	form.first_service.data = ACS.first_service
	form.handler.data = User.query.get_or_404(ACS.handler_id).username
	return render_template('log.html', form = form, category=category)	
	
@main.route('/data/anti_case_consult_<id>', methods=['GET','POST'])
@login_required
def data_anti_case_consult_individual(id):
	name = AntiCaseStart.query.get_or_404(id).name
	category = u'反家暴个案 - ' + name + u'服务记录'
	consults = AntiCaseConsult.query.filter_by(person_id = id)
	acc = [[s.date, s.service, User.query.get_or_404(s.handler_id).username] for s in consults]
	accs = json.dumps(acc)
	return render_template('data.html', jtest=accs, category=category, cate = 6)	
	
@main.route('/data/anti_case_ending_<id>', methods=['GET','POST'])
@login_required
def data_anti_case_ending_individual(id):
	name = AntiCaseStart.query.get_or_404(id).name
	category = u'反家暴个案 - ' + name + u'服务记录'
	ACE = AntiCaseEnding.query.filter_by(person_id = id).first()
	form = AntiCaseEndingDataForm()
	if form.validate_on_submit():
		return render_template('log_success.html')
	form.name.data = name
	form.conclusion_status.data = ACE.conclusion_status
	form.conclusion.data = ACE.conclusion
	form.handler.data = User.query.get_or_404(ACE.handler_id).username
	return render_template('log.html', form = form, category=category)	
	
#@main.route('/data/anti_case_consult', methods=['GET','POST'])
#@login_required
#def data_anti_case_consult():
#	category = u'反家暴个案 - 服务记录'
#	acc = [[AntiCaseStart.query.get_or_404(s.person_id).name, s.date, s.service, s, User.query.get_or_404(s.handler_id).username] for s in AntiCaseConsult.query.all()]
#	accs = json.dumps(acc)
#	return render_template('data.html', jtest=accs, category=category, cate = 7)

#@main.route('/data/anti_consult_ending', methods=['GET','POST'])
#@login_required
#def data_anti_consult():
#	category = u'反家暴咨询'
#	ace = [[s.id, s.service_cate, User.query.filter_by(id=s.user_id).first().username] for s in Service.query.all()]
#	jtest = json.dumps(test)
#	return render_template('data.html', jtest=jtest, category=category)

#=============记录=============
@main.route('/log', methods=['GET', 'POST'])
@login_required
def log():
	funcname = 'log'
	return render_template('log.html', funcname = funcname)

@main.route('/log/legal_case_person', methods=['GET', 'POST'])
@login_required
def log_legal_case_person():
	category = u'法律个案 - 案主档案'
	form = LegalCasePersonForm()
	if form.validate_on_submit():
		lcp = LegalCasePerson(
			name = form.name.data,
			sex = form.sex.data,
			gender_identity = form.gender_identity.data,
			sexual_orientation = form.sexual_orientation.data,
			age = form.age.data,
			contact_info = form.contact_info.data,
			recourse_means = form.recourse_means.data,
			location = form.location.data,
			economic_status = form.economic_status.data,
			case_category = form.case_category.data,
			marriage_status = form.marriage_status.data,
			case_brief = form.case_brief.data,
			legal_needs = form.legal_needs.data,
			previous_recourse = form.previous_recourse.data,
			post_script = form.post_script.data,
			date = form.date.data,
			handler_id = User.query.filter_by(username=current_user.username).first().id,
		)
		db.session.add(lcp)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)

@main.route('/log/legal_case_consult', methods=['GET','POST'])
@login_required
def log_legal_case_consult():
	category = u'法律个案 - 服务记录'
	form = LegalCaseConsultForm()
	form.name.choices = [(lcp.id, lcp.name) for lcp in LegalCasePerson.query.all()]
	if form.validate_on_submit():
		lcc = LegalCaseConsult(
			date = form.date.data,
			consult_brief = form.consult_brief.data,
			following_up = form.following_up.data,
			post_script = form.post_script.data,
			# Foreign Keys
			handler_id = User.query.filter_by(username=current_user.username).first().id,
			person_id = form.name.data
		)
		db.session.add(lcc)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)
	
@main.route('/log/legal_consult', methods=['GET','POST'])
@login_required
def log_legal_consult():
	category = u'法律咨询'
	form = LegalConsultForm()
	if form.validate_on_submit():
		lc = LegalConsult(
			date = form.date.data,
			name = form.name.data,
			sex = form.sex.data,
			gender_identity = form.gender_identity.data,
			sexual_orientation = form.sexual_orientation.data,
			age = form.age.data,
			location = form.location.data,
			recourse_method = form.recourse_method.data,
			consult_category = form.consult_category.data,
			marriage_status = form.marriage_status.data,
			recourse_means = form.recourse_means.data,
			consult_brief = form.consult_brief.data,
			consult_answer = form.consult_answer.data,
			handler_id = User.query.filter_by(username=current_user.username).first().id)
		db.session.add(lc)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)

@main.route('/log/anti_case_doc', methods=['GET', 'POST'])
@login_required
def log_anti_case_doc():
	category=u'反家暴个案-档案信息'
	form = AntiCaseDocForm()
	if form.validate_on_submit():
	    return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)

@main.route('/log/anti_case_person', methods=['GET', 'POST'])
@login_required
def log_anti_case_person():
	category=u'反家暴个案-案主个人信息'
	form = AntiCasePersonForm()
	if form.validate_on_submit():
	    return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)

@main.route('/log/anti_case_service', methods=['GET', 'POST'])
@login_required
def log_anti_case_service():
	category=u'反家暴个案-服务信息'
	form = AntiCaseServiceForm()
	if form.validate_on_submit():
	    return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)

@main.route('/log/anti_case_start', methods=['GET','POST'])
@login_required
def log_anti_case_start():
	category = u'反家暴个案 - 开案'
	form = AntiCaseStartForm()
	if form.validate_on_submit():
		acs = AntiCaseStart(
			time = form.time.data,
			recourse_source = form.recourse_source.data,
			recourse_method = form.recourse_method.data,
			multi_cooperation = form.multi_cooperation.data,
			service_method = form.service_method.data,
			case_brief = form.case_brief.data,
			name = form.name.data,
			sex = form.sex.data,
			gender_identity = form.gender_identity.data,
			sexual_orientation = form.sexual_orientation.data,
			age = form.age.data,
			contact_info = form.contact_info.data,
			location = form.location.data,
			job_status = form.job_status.data,
			job_description = form.job_description.data,
			family_description = form.family_description.data,
			education = form.education.data,
			economic_status = form.economic_status.data,
			relation_status = form.relation.data,
			relation_lasting = form.relation_lasting.data,
			living_status = form.living_status.data,
			risk = form.risk.data,
			other_info = form.other_info.data,
			anti_role = form.anti_role.data,
			relation = form.relation.data,
			case_category = form.case_category.data,
			violent_category = form.violent_category.data,
			violent_category_spirit = form.violent_category_spirit.data,
			violent_category_spirit_other = form.violent_category_spirit_other.data,
			violent_category_strain = form.violent_category_strain.data,
			violent_category_other = form.violent_category_other.data,
			communication_control = form.communication_control.data,
			brief = form.brief.data,
			injury = form.injury.data,
			recourse_others = form.recourse_others.data,
			advocate_suggestions = form.advocate_suggestions.data,
			requirement = form.requirement.data,
			requirement_analysis = form.requirement_analysis.data,
			service_goal = form.service_goal.data,
			cooperation_requirement = form.cooperation_requirement.data,
			resources = form.resources.data,
			social_relation_1 = form.social_relation_1.data,
			social_support_1 = form.social_support_1.data,
			social_relation_2 = form.social_relation_2.data,
			social_support_2 = form.social_support_2.data,
			social_relation_3 = form.social_relation_3.data,
			social_support_3 = form.social_support_3.data,
			first_service = form.first_service.data,
			# Foreign Key
			handler_id = User.query.filter_by(username=current_user.username).first().id
		)
		db.session.add(acs)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)
	
@main.route('/log/anti_case_consult', methods=['GET','POST'])
@login_required
def log_anti_case_consult():
	category = u'反家暴个案 - 服务记录'
	form = AntiCaseConsultForm()
	form.name.choices = [(acs.id, acs.name) for acs in AntiCaseStart.query.all()]
	if form.validate_on_submit():
		acc = AntiCaseConsult(
			date = form.date.data,
			service = form.service.data,
			# Foreign Key
			person_id = form.name.data,
			handler_id = User.query.filter_by(username=current_user.username).first().id
		)
		db.session.add(acc)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)
	
@main.route('/log/anti_case_ending', methods=['GET','POST'])
@login_required
def log_anti_case_ending():
	category = u'反家暴个案 - 结案'
	form = AntiCaseEndingForm()
	form.name.choices = [(acs.id, acs.name) for acs in AntiCaseStart.query.all()]
	if form.validate_on_submit():
		ace = AntiCaseEnding(
			conclusion_status = form.conclusion_status.data,
			conclusion = form.conclusion.data,
			# Foreign Key
			person_id = form.name.data,
			handler_id = User.query.filter_by(username=current_user.username).first().id
		)
		db.session.add(ace)
		db.session.commit()
		return render_template('log_success.html')
	return render_template('log.html', form=form, category=category)
	
#@main.route('/log/anti_consult', methods=['GET','POST'])
#@login_required
#def log_anti_consult():
#	category = u'反家暴咨询'
#	form = AntiConsultForm()
#	form.handler.choices = [(u.id, u.username) for u in User.query.all()]
#	if form.validate_on_submit():
#		handler = User.query.filter_by(username=handler_name).first()
#		if handler is None:
#			return redirect(url_for('log'))
#		else:
#		service = Service(
#			service_cate = form.service_cate.data,
#				date = form.date.data,
#				handler = form.handler.data,
#				channel = form.channel.data,
#				case_cate = form.case_cate.data,
#				brief = form.brief.data,
#				notes = form.notes.data,
#			user_id = form.handler.data)
#		db.session.add(service)
#		db.session.commit()
#		return render_template('log_success.html')
#	return render_template('log.html', form=form, category=category)


@main.route('/')#, methods=['GET', 'POST'])
def index():
#	form = NameForm()
#	if form.validate_on_submit():
#		user = User.query.filter_by(username=form.name.data).first()
#		if user is None:
#			user = User(username = form.name.data)
#			db.session.add(user)
#			session['known'] = False
#		else:
#			session['known'] = True
#		session['name'] = form.name.data
#		form.name.data = ''
#		return redirect(url_for('main.index'))
#	return render_template('index.html',
#		form = form, name = session.get('name'),
#		known = session.get('known', False))
	return render_template('index.html')


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


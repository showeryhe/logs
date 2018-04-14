#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import Required

from werkzeug import generate_password_hash, check_password_hash
class ServiceForm(Form):
	service_cate = StringField(u'服务类别', validators=[Required()])
#	date = StringField('date', validators=[Required()])
	handler = SelectField(u'处理人', coerce = int)
#	channel = SelectField('channel', choices=['QQ', 'weixin', 'E-mail'], validators=[Required()])
#	case_cate = SelectField('case category', choices=['violence', 'legal counsel'], validators=[Required()])
#	brief = TextAreaField('brief introduction to the case', validators=[Required()])
#	notes = TextAreaField('Anything else to mention')
	submit = SubmitField(u'提交')


class NameForm(Form):
	name = StringField(u'用户名', validators=[Required()])
	submit = SubmitField(u'提交')

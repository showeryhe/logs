#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, DateField, SelectField, SelectMultipleField, SubmitField, FormField, RadioField, BooleanField
from wtforms.validators import Required

from werkzeug import generate_password_hash, check_password_hash

class LegalCasePersonForm(Form):
	name = StringField(u'姓名/昵称', validators=[Required()])
	sex = SelectField(u'生理性别', choices=[(u'男', u'男'),(u'女', u'女'),(u'不知',u'不知')])
	gender_identity = SelectField(u'性别认同', choices=[(u'男',u'男'),(u'女', u'女'),(u'不知', u'不知')])
	sexual_orientation = SelectField(u'性倾向', choices=[(u'异性恋', u'异性恋'),(u'泛性恋', u'泛性恋'),(u'其他', u'其他')])
	age = StringField(u'年龄')
	contact_info = StringField(u'联系方式')
	recourse_means = SelectField(u'求助途径', choices=[(u'电话', u'电话'),(u'邮箱', u'邮箱')])
	location = StringField(u'居住地/案件发生地')
	economic_status = StringField(u'经济情况')
	case_category = SelectField(u'案件类型', choices=[(u'婚姻财产',u'婚姻财产'),
			(u'就业歧视',u'就业歧视'),
			(u'生育与收养',u'生育与收养'),
			(u'家庭暴力',u'家庭暴力')])
	marriage_status = BooleanField(u'已婚')
	case_brief = TextAreaField(u'案件概况')
	legal_needs = StringField(u'法律需求') 
	previous_recourse = SelectField(u'求助经历', choices=[(u'报警', u'报警'),(u'妇联', u'妇联'), (u'村、居委会', u'村、居委会'), (u'其他', u'其他'),(u'无', u'无'),(u'不知', u'不知')])
	post_script = TextAreaField(u'备注')
	date = DateField(u'开案日期, 请按照yyyy-mm-dd格式填写')
	submit = SubmitField(u'提交')
	
class LegalCaseConsultForm(Form):
	name = SelectField(u'案主姓名', coerce = int)
	date = DateField(u'服务日期，请按照yyyy-mm-dd格式填写')
	consult_brief = TextAreaField(u'服务信息')
	following_up = TextAreaField(u'后续跟进备忘')
	post_script = TextAreaField(u'其他补充信息')
	submit = SubmitField(u'提交')

class LegalConsultForm(Form):
	date = DateField(u'咨询日期，请按照yyyy-mm-dd格式填写')
	name = StringField(u'姓名/昵称', validators=[Required()])
	sex = SelectField(u'生理性别', choices=[(u'男', u'男'),(u'女', u'女'),(u'不知',u'不知')])
	gender_identity = SelectField(u'性别认同', choices=[(u'男',u'男'),(u'女', u'女'),(u'不知', u'不知')])
	sexual_orientation = SelectField(u'性倾向', choices=[(u'异性恋', u'异性恋'),(u'泛性恋', u'泛性恋'),(u'其他', u'其他')])
	age = StringField(u'年龄')
	location = StringField(u'居住地')
	recourse_method = StringField(u'了解途径')
	consult_category = SelectField(u'咨询问题类型', 
		choices=[(u'婚姻财产',u'婚姻财产'),
			(u'就业歧视',u'就业歧视'),
			(u'校园霸凌',u'校园霸凌'),
			(u'生育与收养',u'生育与收养'),
			(u'家庭暴力',u'家庭暴力')])
	marriage_status = BooleanField(u'婚姻状况')
	recourse_means = SelectField(u'咨询方式',
		choices=[(u'电话', u'电话'),
		(u'邮箱', u'邮箱')])
	consult_brief = TextAreaField(u'咨询问题描述',
		default = u'包括时间、地点、人物、问题、诉求')
	consult_answer = TextAreaField(u'解答')
	submit = SubmitField(u'提交')

class AntiCaseStartForm(Form):
	time = DateField(u'接案日期，请按照yyyy-mm-dd格式填写')
	recourse_source = SelectField(u'案主来源', 
		choices=[(u'直接求助', u'直接求助'), 
		(u'转介', u'转介'), 
		(u'外展活动', u'外展活动（外展活动当场接案）')])		
	recourse_method = SelectField(u'求助途径', 
		choices=[(u'电话', u'电话'), 
			(u'邮件', u'邮件'),
			(u'QQ', u'QQ'), 
			(u'微信', u'微信'),
			(u'线上问卷', u'线上问卷')])
	multi_cooperation = SelectField(u'多方合作',
			choices = [(u'无', u'无'),
			(u'有', u'有')])
	service_method = StringField(u'服务方式', 
		default = u'例：线上视频、电话、面谈')
	case_brief = TextAreaField(u'案情简述', 
		default = u'请用50-100字概括整个案件的全貌')
	name = StringField(u'姓名/昵称')
	sex = SelectField(u'生理性别', 
		choices = [(u'男', u'男'),
		(u'女', u'女'),
		(u'不知', u'不知')])
	gender_identity = SelectField(u'性别认同', 
		choices=[(u'男',u'男'),
		(u'女', u'女'),
		(u'不知', u'不知')])
	sexual_orientation = SelectField(u'性倾向', 
		choices=[(u'异性恋', u'异性恋'),
		(u'同性恋', u'同性恋'),
		(u'双性恋',u'双性恋'),
		(u'其他', u'其他')])
	age = StringField(u'年龄')
	contact_info = StringField(u'联系方式，QQ、微信、电话等')
	location = StringField(u'现居住地')
	job_status = BooleanField(u'是否参加工作/就学')
	job_description = StringField(u'工作/就学情况描述，所在单位/学校、无业/辍学情况')
	family_description = TextAreaField(u'家庭情况，如：家系图、家庭结构、成长背景经历等')
	education = SelectField(u'文化程度',
		choices = [(u'小学以下', u'小学以下'),
		(u'初中', u'初中'),
		(u'高中', u'高中'),
		(u'大学', u'大学'),
		(u'研究生及以上', u'研究生及以上')])
	economic_status = StringField(u'主要经济情况',
		default = u'是否独立、经济来源等')
	relation_status = SelectField(u'情感和婚姻状况',
		choices = [(u'单身中', u'单身中'),
		(u'恋情中', u'恋情中'),
		(u'婚姻中', u'婚姻中')])
	relation_lasting = StringField(u'情感状况持续时间')
	living_status = SelectField(u'居住状况',
		choices = [(u'与亲密关系同居', u'与亲密关系同居'),
		(u'与亲密关系分居', u'与亲密关系分居'),
		(u'与原生家庭分居', u'与原生家庭分居'),
		(u'与原生家庭分居', u'与原生家庭分居')])
		#其他情况请描述
	risk = StringField(u'风险评估表分数')
	other_info = StringField(u'其他重要信息',
		default = u'补充对此案有重要影响的信息')
	anti_role = SelectField(u'在家暴中，案主是', 
		choices= [(u'受暴者', u'受暴者'), (u'相对人', u'相对人'), (u'求助者', u'求助者（非受暴者和相对人）')])
	relation = StringField(u'受暴者和施暴者的关系是')
	case_category = SelectField(u'案件类型', 
		choices=[(u'原生家庭', u'原生家庭'), 
		(u'亲密关系', u'亲密关系')])
	violent_category = SelectField(u'暴力类型',
		choices = [(u'肢体暴力', u'肢体暴力'), 
		(u'精神暴力', u'精神暴力'), 
		(u'经济控制', u'经济控制'), 
		(u'性暴力', u'性暴力'), 
		(u'限制人身自由', u'限制人身自由'), 
		(u'其他', u'其他')])#多选
	violent_category_spirit = SelectField(u'精神暴力细分',
		choices = [(u'辱骂', u'辱骂'), 
		(u'恐吓', u'恐吓'), 
		(u'诽谤', u'诽谤'), 
		(u'裸照威胁', u'裸照威胁'), 
		(u'出柜威胁', u'出柜威胁'), 
		(u'自杀威胁', u'自杀威胁'),
		(u'钱财诈骗', u'钱财诈骗'),
		(u'其他', u'其他')])#多选
	violent_category_spirit_other = StringField(u'描述精神暴力中的其他')
	violent_category_strain = SelectField(u'限制人身自由细分',
		choices = [(u'拘禁在家', u'拘禁在家'), 
		(u'精神病院', u'精神病院'), 
		(u'第三方机构', u'网戒所、军事化管理等第三方机构')])#多选
	violent_category_other = StringField(u'描述暴力类型中的其他')
	communication_control = TextAreaField(u'通讯设备受控状态',
		default = u'（电话、微信等）')
	brief = TextAreaField(u'家暴基本情况及持续时间',
		default = u'（填写尽可能多的案情细节）')
	injury = TextAreaField(u'求助时案主受伤情况')
	recourse_others = TextAreaField(u'其他机构求助情况',
		default = u'这里要做成子表？')
	advocate_suggestions = TextAreaField(u'倡导建议')
	requirement = TextAreaField(u'案主诉求')
	requirement_analysis = TextAreaField(u'需求分析')
	service_goal = TextAreaField(u'服务目标')
	cooperation_requirement = TextAreaField(u'多部门联动需求',
		default = u'（派出所/妇联/居委会/法院/学校/其他机构等的需求）')
	resources = TextAreaField(u'案主主要资源，包括住所、资金等资源')
	social_relation_1 = StringField(u'与受害者关系1')
	social_support_1 = StringField(u'能够提供何种支持1')
	social_relation_2 = StringField(u'与受害者关系2')
	social_support_2 = StringField(u'能够提供何种支持2')
	social_relation_3 = StringField(u'与受害者关系3')
	social_support_3 = StringField(u'能够提供何种支持3')
	first_service = TextAreaField(u'首次介入行动',
		default = u'首次介入行动：情绪疏导、需求分析、确定服务目标、制定服务计划、紧急庇护、紧急援助、送医院、转介等，请根据案情做描述')
	submit = SubmitField(u'提交')
	
class AntiCaseConsultForm(Form):
	name = SelectField(u'案主姓名', coerce =  int, validators=[Required()])
	date = DateField(u'服务日期，请按照yyyy-mm-dd格式填写')
	service = TextAreaField(u'服务纪要', default = u'例： 案主沟通想离开家，制定行动和安全计划 注：每一次跟进服务，服务者都需要记录在表中，体现出更多的案情细节')
	submit = SubmitField(u'提交')

class AntiCaseEndingForm(Form):
	name = SelectField(u'案主姓名', coerce = int, validators=[Required()])
	conclusion_status = SelectField(u'结案信息',
		choices = [(u'未结案', u'未结案'),
		(u'已结案。经服务，案主服务需求已被满足', u'已结案。经服务，案主服务需求已被满足'),
		(u'已结案。经服务，案主具备资源链接能力', u'已结案。经服务，案主具备资源链接能力'),
		(u'已结案。案主失联', u'已结案。案主失联(一个月内不同日期、不同时段联系案主三次,均无法联系上)'),
		(u'已结案。案主没有提供联系方式',
		u'已结案。案主没有提供联系方式'),
		(u'已结案。案主拒绝服务', 
		u'已结案。案主拒绝服务'),
		(u'已结案。案主死亡',
		u'已结案。案主死亡')])
	conclusion = TextAreaField(u'总结与反思',
		default = u'服务中可借鉴的亮点、服务难点等')
	submit = SubmitField(u'提交')

class AntiCaseStartDataForm(Form):
	time = StringField(u'接案日期', validators=[Required()])
	recourse_source = StringField(u'案主来源')
	recourse_method = StringField(u'求助途径') 
	multi_cooperation = StringField(u'多方合作')
	service_method = StringField(u'服务方式') 
	case_brief = TextAreaField(u'案情简述')
	name = StringField(u'姓名/昵称')
	sex = StringField(u'生理性别')
	gender_identity = StringField(u'性别认同')
	sexual_orientation = StringField(u'性倾向')
	age = StringField(u'年龄')
	contact_info = StringField(u'联系方式')
	location = StringField(u'现居住地')
	job_status = BooleanField(u'参加工作/就学')
	job_description = StringField(u'工作/就学情况描述')
	family_description = TextAreaField(u'家庭情况')
	education = StringField(u'文化程度')
	economic_status = StringField(u'主要经济情况')
	relation_status = StringField(u'情感和婚姻状况')
	relation_lasting = StringField(u'情感状况持续时间')
	living_status = StringField(u'居住状况')
	risk = StringField(u'风险评估表分数')
	other_info = StringField(u'其他重要信息')
	anti_role = StringField(u'在家暴中，案主是')
	relation = StringField(u'受暴者和施暴者的关系是')
	case_category = StringField(u'案件类型')
	violent_category = StringField(u'暴力类型')
	violent_category_spirit = StringField(u'精神暴力细分')
	violent_category_spirit_other = StringField(u'描述精神暴力中的其他')
	violent_category_strain = StringField(u'限制人身自由细分')
	violent_category_other = StringField(u'描述暴力类型中的其他')
	communication_control = TextAreaField(u'通讯设备受控状态')
	brief = TextAreaField(u'家暴基本情况及持续时间')
	injury = TextAreaField(u'求助时案主受伤情况')
	recourse_others = TextAreaField(u'其他机构求助情况')
	advocate_suggestions = TextAreaField(u'倡导建议')
	requirement = TextAreaField(u'案主诉求')
	requirement_analysis = TextAreaField(u'需求分析')
	service_goal = TextAreaField(u'服务目标')
	cooperation_requirement = TextAreaField(u'多部门联动需求')
	resources = TextAreaField(u'案主主要资源')
	social_relation_1 = StringField(u'与受害者关系')
	social_support_1 = StringField(u'能够提供何种支持')
	social_relation_2 = StringField(u'与受害者关系')
	social_support_2 = StringField(u'能够提供何种支持')
	social_relation_3 = StringField(u'与受害者关系')
	social_support_3 = StringField(u'能够提供何种支持')
	first_service = TextAreaField(u'首次介入行动')
	handler = StringField(u'接案社工')

class AntiCaseEndingDataForm(Form):
	name = StringField(u'案主姓名', validators=[Required()])
	conclusion_status = StringField(u'结案信息')
	conclusion = TextAreaField(u'总结与反思')
	handler = StringField(u'接案社工')
	
class NameForm(Form):
	name = StringField(u'用户名', validators=[Required()])
	submit = SubmitField(u'提交')

class AntiCaseDocForm(Form):#档案信息
	name = StringField(u'姓名/昵称', validators=[Required()])
	time = StringField(u'接案日期，请按照yyyy-mm-dd格式填写')
	recourse_source = SelectField(u'案主来源', 
		choices=[(u'直接求助', u'直接求助'), 
		(u'转介', u'转介'), 
		(u'外展活动', u'外展活动（外展活动当场接案）')])		
	recourse_method = SelectField(u'求助途径', 
		choices=[(u'电话', u'电话'), 
			(u'邮件', u'邮件'),
			(u'QQ', u'QQ'), 
			(u'微信', u'微信'),
			(u'线上问卷', u'线上问卷')])
	multi_cooperation = BooleanField(u'多方合作')
	service_method = StringField(u'服务方式', 
		default = u'例：线上视频、电话、面谈')
	case_brief = TextAreaField(u'案情简述', 
		default = u'请用50-100字概括整个案件的全貌')
	submit = SubmitField(u'提交')

class AntiCasePersonForm(Form):#案主个人信息
	name = StringField(u'案主姓名', validators=[Required()])
	#name = SelectField(u'案主姓名', coerce=int, validators=[Required()])
	date = StringField(u'服务日期，请按照yyyy-mm-dd格式填写')
	sex = SelectField(u'生理性别', 
		choices = [(u'男', u'男'),
		(u'女', u'女'),
		(u'不知', u'不知')])
	gender_identity = SelectField(u'性别认同', 
		choices=[(u'男',u'男'),
		(u'女', u'女'),
		(u'不知', u'不知')])
	sexual_orientation = SelectField(u'性倾向', 
		choices=[(u'异性恋', u'异性恋'),
		(u'同性恋', u'同性恋'),
		(u'双性恋',u'双性恋'),
		(u'其他', u'其他')])
	age = StringField(u'年龄')
	contact_info = StringField(u'联系方式，QQ、微信、电话等')
	location = StringField(u'现居住地')
	job_status = BooleanField(u'正工作/就学')
	job_description = StringField(u'工作/就学情况描述',
		default = u'所在单位/学校、无业/辍学情况')
	family_description = TextAreaField(u'家庭情况，如：家系图、家庭结构、成长背景经历等')
	education = SelectField(u'文化程度',
		choices = [(u'小学以下', u'小学以下'),
		(u'初中', u'初中'),
		(u'高中', u'高中'),
		(u'大学', u'大学'),
		(u'研究生及以上', u'研究生及以上')])
	economic_status = StringField(u'主要经济情况',
		default = u'是否独立、经济来源等')
	relation_status = SelectField(u'情感和婚姻状况',
		choices = [(u'单身中', u'单身中'),
		(u'恋情中', u'恋情中'),
		(u'婚姻中', u'婚姻中')])
	relation_lasting = StringField(u'情感状况持续时间')
	intimate_living = SelectField(u'与亲密关系居住状况',
		choices = [(u'与亲密关系同居', u'与亲密关系同居'),
		(u'与亲密关系分居', u'与亲密关系分居')])
	origin_living = SelectField(u'与原生家庭居住状况',
		choices = [(u'与原生家庭分居', u'与原生家庭分居'),
		(u'与原生家庭分居', u'与原生家庭分居')])
	living_ps = StringField(u'居住状况的其他描述')
	risk = StringField(u'风险评估表分数')
	other_info = StringField(u'其他重要信息',
		default = u'补充对此案有重要影响的信息')
	submit = SubmitField(u'提交')

class AntiCaseServiceForm(Form):#服务信息
	#name = SelectField(u'案主姓名', coerce =  int, validators=[Required()])
	name = StringField(u'案主姓名')
	#date = StringField(u'服务日期，请按照yyyy-mm-dd格式填写')
	anti_role = SelectField(u'在家暴中，案主是', 
		choices = [(u'受暴者', u'受暴者'),
		(u'相对人', u'相对人'),
		(u'求助者', u'求助者（非受暴者和相对人）')])
	relation = StringField(u'受暴者和施暴者的关系是')#这个需要改成单选项吗
	case_category = SelectField(u'案件类型', 
		choices=[(u'原生家庭', u'原生家庭'), 
		(u'亲密关系', u'亲密关系')])
	physical_vio = BooleanField(u'肢体暴力')
	swear = BooleanField(u'辱骂')
	intimidate = BooleanField(u'恐吓')
	defame = BooleanField(u'诽谤')
	naked_photo = BooleanField(u'落照威胁')
	outed = BooleanField(u'出柜威胁')
	suicide = BooleanField(u'自杀威胁')
	self_harm = BooleanField(u'自伤威胁')
	property_fraud = BooleanField(u'钱财诈骗')
	spiritual_vio = StringField(u'其他精神暴力')
	economic_controlled = BooleanField(u'经济控制')
	sexual_vio = BooleanField(u'性暴力')
	confined = BooleanField(u'拘禁在家')
	institution_hos = BooleanField(u'精神病院')
	institution_others = BooleanField(u'网戒所、军事化管理等第三方机构')
	other_vio = StringField(u'其他暴力')
	communication_control = TextAreaField(u'通讯设备受控状态',
		default = u'（电话、微信等）')
	brief = TextAreaField(u'家暴基本情况及持续时间',
		default = u'（填写尽可能多的案情细节）')
	injury = TextAreaField(u'求助时案主受伤情况')
	recourse_police = BooleanField(u'求助警察')
	recourse_police_description = StringField(u'求助警察情况')
	recourse_police_count = StringField(u'求助警方次数')
	recourse_police_respond = BooleanField(u'出警')
	recourse_police_respond_description = StringField(u'出警事由/未出警反馈')
	recourse_police_case = BooleanField(u'立案')
	recourse_police_case_description = StringField(u'立案案由/未立案原因')
	recourse_police_evidence = BooleanField(u'取证')
	recourse_police_evidence = StringField(u'取证证据/未取证缘由')
	recourse_police_record = SelectField(u'出警记录',
		choices=[(u'警方出动提供', u'警方出动提供'),
			(u'报警人提出要求', u'报警人提出要求，警方提供'),
			(u'警方未主动提供', u'警方未主动提供'),
			(u'报警人提出要求被拒绝', u'报警人提出要求被拒绝')])
	recourse_police_effect = StringField(u'警察介入效果')
	recourse_wu = BooleanField(u'求助妇联')
	recourse_wu_description = StringField(u'求助妇联情况')
	recourse_wu_count = StringField(u'求助妇联次数')
	recourse_wu_inter = BooleanField(u'妇联介入干预')
	recourse_wu_inter_description = StringField(u'妇联干预案由/未干预缘由')
	recourse_wu_effect = StringField(u'妇联介入效果',
		default = u'实施措施、对暴力的影响、后续跟进情况等')
	recourse_st = BooleanField(u'求助街道办事处/居委会/村委会等')
	recourse_st_description(u'求助情况',
		default = u'地区、时间、人物、事件描述')
	recourse_st_count = StringField(u'居民组织求助次数')
	recourse_st_inter = BooleanField(u'居民组织介入干预')
	recourse_st_inter_description = StringField(u'居民组织干预案由/未干预缘由')
	recourse_st_effect = StringField(u'居民组织介入效果',
		default = u'实施措施、对暴力的影响、后续跟进情况等')
	
	recourse_psy = SelectField(u'心理、精神科求助',
		choices = [(u'无', u'无'),
			(u'心理咨询师', u'心理咨询师'),
			(u'精神科医师', u'精神科医师')])
	recourse_psy_description = StringField(u'心理、精神科求助情况',
		default = u'机构/个人名称、是否有偿、咨询次数、时间、地点等')
	recourse_psy_reason = StringField(u'心理、精神科求助案由及诉求')
	recourse_psy_effect = StringField(u'心理、精神科求助效果')
		
	recourse_psy = SelectField(u'法律求助',
		choices = [(u'无', u'无'),
			(u'商业律师', u'商业律师'),
			(u'法律援助', u'法律援助'),
			(u'司法机关', u'司法机关')])
	recourse_psy_description = StringField(u'法律求助情况',
		default = u'机构/个人名称、是否有偿、咨询次数、时间、地点等')
	recourse_psy_reason = StringField(u'案由及诉求')
	recourse_psy_effect = StringField(u'求助效果')
	

	recourse_psy = SelectField(u'心理、精神科求助',
		choices = [(u'无', u'无'),
			(u'心理咨询师', u'心理咨询师'),
			(u'精神科医师', u'精神科医师')])
	recourse_psy_description = StringField(u'求助情况',
		default = u'机构/个人名称、是否有偿、咨询次数、时间、地点等')
	recourse_psy_reason = StringField(u'案由及诉求')
	recourse_psy_effect = StringField(u'求助效果')
	


	recourse_psy = SelectField(u'心理、精神科求助',
		choices = [(u'无', u'无'),
			(u'心理咨询师', u'心理咨询师'),
			(u'精神科医师', u'精神科医师')])
	recourse_psy_description = StringField(u'求助情况',
		default = u'机构/个人名称、是否有偿、咨询次数、时间、地点等')
	recourse_psy_reason = StringField(u'案由及诉求')
	recourse_psy_effect = StringField(u'求助效果')
	






	advocate_suggestions = TextAreaField(u'倡导建议')
	requirement = TextAreaField(u'案主诉求')
	requirement_analysis = TextAreaField(u'需求分析')
	service_goal = TextAreaField(u'服务目标')
	cooperation_requirement = TextAreaField(u'多部门联动需求',
		default = u'（派出所/妇联/居委会/法院/学校/其他机构等的需求）')
	resources = TextAreaField(u'案主主要资源，包括住所、资金等资源')
	social_relation_1 = StringField(u'与受害者关系1')
	social_support_1 = StringField(u'能够提供何种支持1')
	social_relation_2 = StringField(u'与受害者关系2')
	social_support_2 = StringField(u'能够提供何种支持2')
	social_relation_3 = StringField(u'与受害者关系3')
	social_support_3 = StringField(u'能够提供何种支持3')
	first_service = TextAreaField(u'首次介入行动',
		default = u'首次介入行动：情绪疏导、需求分析、确定服务目标、制定服务计划、紧急庇护、紧急援助、送医院、转介等，请根据案情做描述')
	submit = SubmitField(u'提交')

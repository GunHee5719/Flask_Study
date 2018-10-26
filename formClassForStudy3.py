from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# 텍스트 입력과 제출 벝튼 하나를 가지는 클래스이다.
class NameForm(Form):
  name = StringField('What is your name?', validators=[Required()])
  submit = SubmitField('Submit')
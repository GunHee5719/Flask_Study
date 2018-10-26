# https://cozy-ho.github.io/flask/2017/10/19/flask-day04.html 페이지를 참고하여 공부 진행.

# 이 파일에서는 웹 폼을 사용하여 웹 사이트 또는 애플리케이션이 서로 상호작용할 수 있도록 웹 사이트에 데이터를 전송하는 작업을 진행한다.
# 플라스크에서는 Flask-wtf 확장을 통해 CSRF (리퀘스트 위조) 공격으로부터 폼을 보호한다.
# pip install flask-wtf 명령어를 통해 설치 가능하다 (파이참에서는 자동 설치해준다)

# template 폴더 안에 index.html 파일을 만들었으며, 그 안에는 내용을 담았다. 이 때 Jinja2의 조건문 포맷을 사용했다! 자세한 내용은 해당 파일 참고

# Flask 프레임워크를 import하며, Jinja2 template engine 통합을 위해 함께 import 해준다.
from flask import Flask, render_template

# NameForm 함수를 사용할 것이다. 같은 디렉토리에 form class를 만든다.
from formClassForStudy3 import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

# GET 리퀘스트에는 본문이 없고 쿼리 그대로 출력되기 때문에 보안상 좋지 않으므로 POST를 추가해준다.
@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  form = NameForm()
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
  return render_template('form.html', form=form, name=name)

if __name__ == '__main__':
    app.run(debug=True)
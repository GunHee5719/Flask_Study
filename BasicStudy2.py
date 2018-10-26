# https://cozy-ho.github.io/flask/2017/10/16/flask-day03.html 페이지를 참고하여 공부 진행.

# 이 파일에서는 신사2 템플릿엔진을 사용하는 것을 다룬다.
# template 폴더를 생성하여 안에 BasicStudy2.html 파일을 만들었으며, 그 안에는 다음 내용을 담는다.
# <h1>Hello, {{name}}!</h1>

# {{name}} 부분은 변수를 뜻하며, 렌더링되는 시점에서의 데이터로부터 얻어오는 값을 의미한다. 어떤 타입을 써도 인식한다.
# 만약 {{name}} 을 {{name | apitalize}} 를 쓴다면, 변수의 첫 문자를 대문자로 한다. 즉, |를 분리자로 하여 필터를 사용할 수 있다.

# Flask 프레임워크를 import하며, Jinja2 template engine 통합을 위해 함께 import 해준다.
from flask import Flask, render_template

app = Flask(__name__)

# BasicStudy 에서의 내용과 같으며, 그냥 127.0.0.1:5000 호출 시 HELLO WORLD 를 출력한다.
@app.route('/')
def hello():
    return '<h1>HELLO WORLD!</h1>'

# 신사2 템플릿엔진을 렌더링함으로서, 아래의 URL로 입력될 시(ex. 127.0.0.1:5000/user/gunhee) BasicStudy2.html 이 실행된다.
@app.route('/user/<name>')
def user(name):
    return render_template('BasicStudy2.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
# https://cozy-ho.github.io/flask/2017/10/13/flask-day02.html 페이지를 참고하여 공부 진행.
# Flask 프레임워크를 사용하기 위해 import 진행
from flask import Flask

# 인스턴스 생성, 웹 서버는 client로부터 수신한 request를 이 object에서 처리한다.
app = Flask(__name__)

# [1] 기초 출력
# Client는 요청 URL을 함수에 매핑하는데, 이를 app.route로 진행한다. 이 때 최상위 디렉토리('/') 를 매핑하였다.
@app.route('/')
def hello():
    return '<h1>HELLO WORLD</h1>'


# [2] 인자 전달
# Client의 요청에서 꺽쇠 내의 내용을 가져다 사용할 수 있다.
# 예를 들어 127.0.0.1:5000/user/건희 로 접근할 시 "HELLO, 건희!" 가 출력된다.
@app.route('/user/<name>')
def user(name):
    return '<h1>HELLO, %s!</h1>' %name


if(__name__) == '__main__':
    # debug = True 를 지정함으로서 웹 앱이 실행중에 오류가 생겼을 때 브라우저에서 Operation 모드를 설정할 수 있도록 함.
    # 개발 시 디버그 모드를 사용할 수 있기 때문에 실제 웹 서버에 올릴 때는 꼭 삭제해야 한다!
    app.run(debug=True)
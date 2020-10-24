from flask import Flask, g, request, Response, make_response
from flask import session
from datetime import datetime, date, timedelta

app = Flask(__name__)  # flask 생성
app.debug = True  # 에러 정보 더 많이 알려준다.

app.config.update(
    SECRET_KEY='X1243yRH!mMwf',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days  cf. minutes=30
)

# 다음 형태로 요청했요청했을때 해당 key로 Cookie를 굽는 코드를 작성하시오.
# http://localhost:5000/wc?key=token&val=abc


@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123X'
    return make_response(res)

# 다음과 같이 요청했을때 해당 key의 Cookie Value를 출력하는 코드를 작성하시오.
# http://localhost:5000/rc?key=token


@app.route('/rc')
def rc():
    key = request.args.get('key')  # token
    val = request.cookies.get(key)
    return "cookie[" + key + "] =" + val + " , " + session.get('Token')


@app.route('/delsess')
def delsess():
    if session.get('Token'):  # 값이 존재 할 때
        del session['Token']
    return "Session이 삭제되었습니다!"
# @app.route('/reqenv')
# def reqenv():
#     return ('REQUEST_METHOD: % (REQUEST_METHOD) s < br >'
#             'SCRIPT_NAME: % (SCRIPT_NAME) s < br > '
#             'PATH_INFO: % (PATH_INFO) s < br > '
#             'QUERY_STRING: % (QUERY_STRING) s < br > '
#             'SERVER_NAME: % (SERVER_NAME) s < br > '
#             'SERVER_PORT: % (SERVER_PORT) s < br > '
#             'SERVER_PROTOCOL: % (SERVER_PROTOCOL) s < br > '
#             'wsgi.version: % (wsgi.version) s < br > '
#             'wsgi.url_scheme: % (wsgi.url_scheme) s < br > '
#             'wsgi.input: % (wsgi.input) s < br > '
#             'wsgi.errors: % (wsgi.errors) s < br > '
#             'wsgi.multithread: % (wsgi.multithread) s < br > '
#             'wsgi.multiprocess: % (wsgi.multiprocess) s < br > '
#             'wsgi.run_once: % (wsgi.run_once) s') % request.environ


def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans


@app.route('/dt')
def dt():
    datestr = request.values.get(
        'date', date.today(), type=ymd('%Y-%m-%d'))  # ('date',defalut값,type)
    return "우리나라 시간 형식: " + str(datestr)

# app.config['SERVER_NAME'] = 'local.com:5000'


# @app.route("/sd")
# def helloworld_local():
#     return "hello local.com!"


# @app.route("/sd", subdomain="g")
# def helloworld22():
#     return "hello g.local.com!"


@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return "q= %s" % str(q)


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),
                   ('Content-Length', str(len(body)))]
        start_response('200 ok', headers)
        return [body]

    return make_response(application)


@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)


@app.before_request  # 매번 request요청을 처리하기 전에 실행
def before_request():
    print("before_request!!")
    g.str = "한글"  # 1. 여기서 g에 한글을 넣어두면


@app.route("/gg")  # URI정의
def helloworld2():
    return "hello flask world!" + getattr(g, 'str', '111')  # 1. 여기서 계속 사용


@app.route("/")
def helloworld():
    return "hello flask world!!!!!!!"

from flask import Flask, request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Practicing Cookies!</h1>"

@app.route("/addCookie")
def addCookie():
 response = make_response("<h1>Cookie added!</h1>");
 response.set_cookie("myFirstCookie","Hello World - my first cookie!")
 return response

@app.route("/displayCookieValue", methods=["GET"])
def displayCookieValue():
 cookieValue = None
#try catch of cookie code
 try:
    cookieValue = request.cookies.get("myFirstCookie")
    return "<h1>Found the cookie: " + cookieValue + "</h1>"
 except:
    return "<h1>Cookie not found!</h1>"

@app.route("/removeCookie")
def removeCookie():
    res = make_response("Cookie removed!")
    res.set_cookie('myFirstCookie', 'myFirstCookie', max_age=0)
    return res

app.run(host='0.0.0.0', port=88)
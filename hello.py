from flask import Flask
from flask import redirect
import logging

app = Flask(__name__)
log = logging.getLogger("web")

@app.route('/')
def index():
    return redirect('http://aajtak.com')
@app.route('/user/<name>')
def user(name):
    log.info("got the user ", name)
    return '<h1> Hello {} </h1>'.format(name)


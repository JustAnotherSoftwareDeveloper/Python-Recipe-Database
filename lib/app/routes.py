from app import app
import datetime

from flask.json import jsonify


@app.route('/')
@app.route('/status')
def index():
    response = {'status':"OK",'Time':datetime.datetime.now(),'project':'recipes'}
    return jsonify(response)
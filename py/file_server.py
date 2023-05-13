from flask import Flask, jsonify
from dataBase import DataBase
from gevent import pywsgi
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/AllPatientData',methods=['GET'])
def getAllPatientData():
    db=DataBase()
    return jsonify(db.getTable("Patient"))
@app.route('/api/shutdown',methods=['POST'])
def shutdown():
    server.stop()
    return jsonify({"content":"stop the server"})
with app.app_context():
    server = pywsgi.WSGIServer(('0.0.0.0',8090),app)
    server.serve_forever()






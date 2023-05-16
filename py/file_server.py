from flask import Flask, jsonify,request
from dataBase import DataBase
from gevent import pywsgi
from flask.json import JSONEncoder
from flask_cors import CORS
from datetime import date

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
CORS(app)
# @app.route('/api/AllPatientData',methods=['GET'])
# def getAllPatientData():
#     db=DataBase()
#     return jsonify(db.getView("patientallinformation_view"))
# @app.route('/api/AllDeptData',methods=['GET'])
# def getAllDeptData():
#     db=DataBase()
#     return jsonify(db.getView("`deptview`"))
# @app.route('/api/AllDoctorData',methods=['GET'])
# def getAllDoctorData():
#     return jsonify(DataBase().getTable("`cs2305.doctor`"))
# @app.route('/api/update',methods=['POST'])
# def update():
#     cmd=request.get_json()
#     table,id,col,value=cmd['table'],cmd['id'],cmd['col'],cmd['value']
#     return jsonify(DataBase().update(table,id,col,value))
@app.route('/api/table',methods=['POST'])
def getTable():
    table=request.get_json()['table']
    return jsonify(DataBase().getTable(table))

@app.route('/api/test',methods=['GET'])
def test():
    table="`cs2305.patient`"
    return jsonify(DataBase().getTable(table))

@app.route('/api/update',methods=['POST'])
def update():
    cmd=request.get_json()
    table,id,col,value=cmd['table'],cmd['id'],cmd['col'],cmd['value']
    return jsonify(DataBase().update(table,id,col,value))
@app.route('/api/shutdown',methods=['POST'])
def shutdown():                       
    server.stop()
    return jsonify({"content":"stop the server"})
with app.app_context():
    server = pywsgi.WSGIServer(('0.0.0.0',8090),app)
    server.serve_forever()






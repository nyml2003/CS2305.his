from flask import Flask, jsonify,request
from dataBase import DataBase
from gevent import pywsgi
from flask_cors import CORS
from datetime import date,datetime,timedelta
from flask.json.provider import DefaultJSONProvider
from decimal import Decimal
# from pytz import timezone
class UpdatedJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            elif isinstance(obj,Decimal):
                return str(obj)
            return super(DefaultJSONProvider, self).default(obj)
        except Exception as e:
            print(obj)
            print(type(obj))
            

app = Flask(__name__)
app.json = UpdatedJSONProvider(app)
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
@app.route('/api/update',methods=['POST'])
def update():
    cmd=request.get_json()
    table,id,col,value,pk=cmd['table'],cmd['id'],cmd['col'],cmd['value'],cmd['pk']
    return jsonify(DataBase().update(table,id,col,value,pk))
@app.route('/api/delete',methods=['POST'])
def delete():
    cmd=request.get_json()
    table,id,pk=cmd['table'],cmd['id'],cmd['pk']
    return jsonify(DataBase().delete(table,id,pk))
@app.route('/api/insert',methods=['POST'])
def insert():
    cmd=request.get_json()
    table,values=cmd['table'],cmd['values']
    return jsonify(DataBase().insert(table,values))
@app.route('/api/shutdown',methods=['POST'])
def shutdown():                       
    server.stop()
    return jsonify({"content":"stop the server"})
with app.app_context():
    server = pywsgi.WSGIServer(('0.0.0.0',8090),app)
    server.serve_forever()






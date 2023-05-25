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
@app.route('/api/table',methods=['POST'])
def getTable():
    table=request.get_json()['table']
    return jsonify(DataBase().getTable(table))
@app.route('/api/view',methods=['POST'])
def getView():
    view=request.get_json()['view']
    return jsonify(DataBase().getView(view))
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
@app.route('/api/login',methods=['POST'])
def login():
    data=request.get_json()
    username,password=data['username'],data['password']
    ret=DataBase().search("`cs2305.user`","username",username)
    if (ret['error']==True and ret['content']!=()):
        print(ret)
        if ret['content'][0]['password']==password:
            return jsonify({
                "isRight":True,
                'user':{
                    "uid":ret['content'][0]['uid'],
                    "username":username,
                    "role":ret['content'][0]['role']
                }
            })
        else:
            return jsonify({
                "isRight":False,
            })
    else:
        return jsonify({
            "isRight":False,
        })
@app.route('/api/register',methods=['POST'])
def register():
    data=request.get_json()
    username,password,role=data['username'],data['password'],data['role']
    ret=DataBase().search("`cs2305.user`","username",username)
    if (ret['error']==True and ret['content']!=()):
        return jsonify({
            "isRight":False,
        })
    else:
        DataBase().register(username,password,role)
        ret=DataBase().search("`cs2305.user`","username",username)
        return jsonify({
            "isRight":True,
            'user':{
                "uid":ret['content'][0]['uid'],
                "username":username,
                "role":role
            }
        })
@app.route('/api/SP',methods=['POST'])
def select_profile():
    uid=request.get_json()['uid']
    res=DataBase().search("`cs2305.user`","uid",uid)['content'][0]
    del res['password']
    if res['role']=="patient":
        res['role']="患者"
        vector=DataBase().search("`cs2305.patient`","uid",uid)['content']
        if vector!=(): res={**res,**vector[0]}
    elif res['role']=="doctor":
        res['role']="医生"
        vector=DataBase().search("`cs2305.doctor`","uid",uid)['content']
        if vector!=(): res={**res,**vector[0]}
    return jsonify(res)
@app.route('/api/shutdown',methods=['POST'])
def shutdown():                       
    server.stop()
    return jsonify({"content":"stop the server"})
with app.app_context():
    server = pywsgi.WSGIServer(('0.0.0.0',8090),app)
    server.serve_forever()






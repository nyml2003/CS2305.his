import pymysql
from pymysql.constants import CLIENT
class DataBase():
    def __init__(self):
        self.conn = pymysql.connect(
            host="124.71.219.185",
            port = 3306, 
            user="root",
            password="uestc2022!",
            database="cs2305.his",
            charset="utf8",
            client_flag=CLIENT.MULTI_STATEMENTS
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    def execute(self,sql, params=None):
        try: 
            self.cursor.execute(sql,params)
            self.conn.commit()
        except:
            self.conn.rollback()
        ret = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return ret
    def getTable(self,table):
        sql=f"SELECT * FROM {table}"
        return self.execute(sql)
    def update(self,table,id,col,value):
        sql = f"SELECT {col} FROM {table} WHERE id = %s"
        res = self.execute(sql, (id,))
        if res is not None and res[0] == value:
            return
        else:
            sql = f"UPDATE {table} SET {col} = %s WHERE id = %s"
            self.cursor.execute(sql,(value,id))
            return



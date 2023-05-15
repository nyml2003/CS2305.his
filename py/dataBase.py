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
        self.cursor = self.conn.cursor()
    def execute(self,sql):
        try: 
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        ret = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return ret
    def getTable(self,TABLE_NAME):
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        ret = self.cursor.fetchall()
        self.cursor.close()
        return ret
    def getView(self,VIEW_NAME):
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(f"SELECT * FROM {VIEW_NAME}")
        ret = self.cursor.fetchall()
        self.cursor.close()
        return ret
    def close(self):
        self.cursor.close()
        self.conn.close()



import pymysql


class DBHelper:
    def __init__(self, db):
        self.db = db

    def connect(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", db=self.db, charset="utf8")
        self.cursor = self.conn.cursor()
    #查询所有
    def queryAll(self, sql, params=[]):
        result = None
        # 执行连接
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return result
    #查询一条
    def queryOne(self, sql, params=[]):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return result
    #增删改
    def update(self, sql, params=[]):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return count

    def close(self):
        self.cursor.close()
        self.conn.close()
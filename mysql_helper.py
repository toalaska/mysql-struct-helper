# encoding:utf-8
import pymysql
#默认的连接参数
class MysqlHelper:
    # 构造函数
    def __init__(self, host=None, user=None,
                 pwd=None, db=None, port=3306):

        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None
        self.port = port

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db, charset='utf8mb4', port=self.port)
        except Exception as e:
            print("连接数据库失败",e)
            raise

        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            print("执行sql失败",e)
            self.close()
            raise



        return True

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        fields = []
        for field in self.cur.description:
            fields.append(field[0])
        res=[]
        for row in self.cur.fetchall():
            one={}
            for i,v in enumerate(row):
                one[fields[i]]=v
            res.append(one)
        return res

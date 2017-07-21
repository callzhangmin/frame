# -*- coding:utf-8 -*-
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
from time import strftime,gmtime
#=========读取db_config.ini文件设置====
base_dir = str(os.path.dirname(os.path.abspath(__file__)))       #返回py脚本的绝对路径
base_dir = base_dir.replace('\\', '/')                           #str.replace(old, new[, max])用新的字符串替换旧的字符串
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()   #ConfigParser 是用来读取配置文件的包,使用前必须先实例化
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")

#========封装mysql基本操作============
class DB:
    def __init__(self):
        #连接数据库
        try:
            self.conn = connect(
                host=host,
                user=user,
                port=int(port),
                password=password,
                db=db,
                charset='utf8mb4',
                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("mysql Error %d: %s" % (e.args[0], e.args[1])
            )

    #清除数据库
    def clear(self,table_name):
        real_sql = "truncate table "+table_name+";"
        # real_sql = "delete from" + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")  #Mysql中如果表和表之间建立的外键约束，则无法删除表及修改表结构,语句作用就是取消外键约束
            cursor.execute(real_sql)   #执行语句
        self.conn.commit()  #如果不用commit,那数据就不会保留在数据库中

    #插入数据
    def insert(self,table_name, table_data):
        for key in table_data:
             table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()


    #关闭数据库的连接
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    db = DB()
    table_name = "sign_event"
    data = {'id':15,'name':'红米4','`limit`':2000,'status':0,'address':'杭州会展中心','start_time':'2017-08-20 00:22:34','create_time':time1}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()


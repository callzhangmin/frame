import sys
sys.path.append('../db_fixture') #对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中
from frame.db_fixture.mysql_db import DB
import time


#创建测试数据
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
datas = {
    # 发布会数据
    'sign_event':[
        {'id': 1, 'name': '红米1发布会', '`limit`': 1000, 'status': 1, 'address': '北京会展中心',
         'start_time': '2017-08-20 00:22:34', 'create_time': time1},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心',
         'start_time': '2017-08-20 00:22:34', 'create_time': time1},
        {'id': 3, 'name': '当前状态为0，关闭', '`limit`': 1000, 'status': 0, 'address': '北京会展中心',
         'start_time': '2017-08-20 00:22:34', 'create_time': time1},
        {'id': 4, 'name': '发布会已结束', '`limit`': 1000, 'status': 0, 'address': '北京会展中心',
         'start_time': '2011-08-20 00:22:34', 'create_time': time1},
        {'id': 5, 'name': '小米5发布会', '`limit`': 1000, 'status': 0, 'address': '北京国际会议中心',
         'start_time': '2017-08-20 00:22:34', 'create_time': time1},
    ],
    'sign_guest':[
        # 嘉宾数据
        {'id':1, 'realname':'alen', 'phone':13512344321, 'email':'alen@qq.com', 'sign':0, 'create_time': time1, 'event_id':1},
        {'id':2, 'realname':'zhang', 'phone':13512344322, 'email':'zhang@qq.com', 'sign':1, 'create_time': time1, 'event_id':1},
        {'id':3, 'realname':'min', 'phone':13512344331, 'email':'min@qq.com', 'sign':0, 'create_time': time1, 'event_id':5},
        {'id':4, 'realname':'xiao', 'phone':13512345321, 'email':'xiao@qq.com', 'sign':1, 'create_time': time1, 'event_id':1},
    ]
}

#将测试数据导入到数据库
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()

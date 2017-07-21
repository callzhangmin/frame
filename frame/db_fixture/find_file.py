import os
result_dir = 'C:\\Users\\js\\Desktop\\guest-master\\frame\\report'

lists = os.listdir(result_dir)  #获得指定目录中的内容
#按照文件创建的时间进行排序
lists.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn))
print(('最新的测试报告为： ' + lists[-1]))
file = os.path.join(result_dir, lists[-1])
print(file)

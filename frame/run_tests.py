import time, sys, os
sys.path.append('./interface')
sys.path.append('./db_fixture')
from frame.HTMLTestRunner import HTMLTestRunner
import unittest
from frame.db_fixture import test_data

#指定测试用例集的路径为当前文件夹下的interface文件夹
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')  #递归查找指定目录（start_dir）及其子目录下的全部测试模块，将这些测试模块放入一个TestSuite 对象并返回。只有匹配pattern的测试文件才会被加载到TestSuite中


if __name__ == '__main__':
    test_data.init_data()
    dir1 = os.path.dirname(__file__)
    now = time.strftime("%Y%m%d %H%M%S")
    filename = dir1+'/report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='test report',
        description='Implementation Example with:'
    )
    runner.run(discover)
    fp.close()





# 导入我们自己新建的包
import pydemo.test9.util.helloUtil as helloUtil

helloUtil.sayHello('言曌')

# 导入官方的包
# math
import math

print(math.pi, math.e)  # 输出π，e
print(math.pow(2, 10))  # 求2的十次方
print(math.sin(0), math.cos(0))  # 求sin，cos
print(math.sqrt(4))  # 开平方根
print(math.ceil(1.5), math.floor(1.5))  # 向上取整，向下取整
print(math.fmod(10, 3))  # 10%3 取模
print()

# random
import random

print(random.random())  # [0,1)的随机小数
print(random.randint(1, 20))  # [a,b]之间的整数
print(random.choice([1, 2, 3, 4, 5]))  # 从列表里获取数
print(random.randrange(10))  # [0,x)之间的整数

# os
import os

print(os.cpu_count())  # CPU个数
print(os.getcwd())  # 当前目录
print(os.sep)  # 分隔符
print(os.listdir('/Users/liuyanzhao/pycode/demo'))  # 该目录的文件列表
# os.rename('/Users/liuyanzhao/pycode/demo/test1.txt',
#           '/Users/liuyanzhao/pycode/demo/test2.txt')  # 文件重命名
# os.mkdir("/Users/liuyanzhao/pycode/demo/test1") # 新建文件夹

# os.rmdir("/Users/liuyanzhao/pycode/demo/test1") # 删除文件夹
# os.remove('/Users/liuyanzhao/pycode/demo/test2.txt')  # 删除文件

# os.path
print(os.path.exists('/Users/liuyanzhao/pycode/demo'))  # 文件是否存在
print(os.path.getsize('/Users/liuyanzhao/pycode/demo/pydemo/test1.py'))  # 获取文件大小
print(os.path.isfile('/Users/liuyanzhao/pycode/demo/pydemo/test1.py'))  # 是否为文件
print(os.path.isdir('/Users/liuyanzhao/pycode/demo/pydemo'))  # 是否为文件夹

# sys
import sys

print(sys.path)  # 环境变量path
print(sys.prefix)  # .venv路径

# time
import time

print(time.time())  # 当前时间戳
print(time.localtime())  # 结构化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 格式化显示
# time.sleep(1)  # 线程睡眠1秒

# datetime
import datetime

print(datetime.datetime.now())
d1 = datetime.datetime(2024, 3, 18, 17, 52)  # 2024年3月18日17:52
print(d1)

# hashlib
import hashlib

md = hashlib.md5()
md.update('123456'.encode('utf-8')) # 对12345 进行md5加密
print(md.hexdigest())

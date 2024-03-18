# 示例1，读取所有
f = open('/Users/liuyanzhao/pycode/demo/text1.txt', 'r')  # 打开文件
# 读取全部内容
content = f.read()
print(content)
f.close()  # 关闭文件

# 示例2，读取一行
f2 = open('/Users/liuyanzhao/pycode/demo/text1.txt', 'r')  # 打开文件
#  读取一行，前10个字符
lineContent = f2.readline(10)
print(lineContent)
# 再读取下一行，前10个字符
lineContent = f2.readline(10)
print(lineContent)

# 示例3，读取所有行，返回列表
f3 = open('/Users/liuyanzhao/pycode/demo/text1.txt', 'r')  # 打开文件
#  读取多行，返回列表
multiLineContent = f3.readlines()
print(multiLineContent)

# 示例4，文件写入（覆盖）
f4 = open('/Users/liuyanzhao/pycode/demo/text1.txt', 'w')  # 打开文件，覆盖内容
f4.write('Hello World')  # 直接全部覆盖
f4.close()

# 示例5，文件写入（追加）
f5 = open('/Users/liuyanzhao/pycode/demo/text1.txt', 'a')  # 打开文件，追加内容
f5.write('\nHello World222')  # 在末尾行追加
# f5.seek()可以移动光标位置
f5.close()

# 示例6，不需要手动调用close的方法 （防止异常情况没有及时调用close方法）
with open('/Users/liuyanzhao/pycode/demo/text1.txt', 'r') as f6:  # 打开文件
    content2 = f6.read()
    print(content2)
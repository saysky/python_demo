# Python 3.7.4
class Person:
    name = '我是类方法属性'

    @classmethod
    def sayHello(cls):
        print('类方法 Hello')

    def __init__(self):
        self.name = '我是实例的属性'

    def sayHello(self):
        print('我是实例方法 Hello222')


# p = Person  # 不会调用 def __init__(self)
# print(p.name) # 调用类的

p = Person()  # 不会调用 def __init__(self)
print(p.name)  # 调用实例的
p.sayHello() # 调用实例的

## 输出内容如下：
# 我是实例的属性
# 我是实例方法 Hello222

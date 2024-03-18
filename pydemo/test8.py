# Python 3.7.4
class Goods:  # 商品类
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sayHello(self):
        print('Hello', self.name, self.price)


g = Goods('小米14', 4399)
g.sayHello()

# 1. type 获取变量的类型
print(type(g))
print(type(g.name))

# 2. dir 获取变量所有属性或方法
print(dir(g))

# 3.isinstance 判断类型
print(isinstance(g, Goods))  # 如果继承了父类，判断是不是父类，也为True

# 4. setattr 设置属性
setattr(g, 'name', '小米14 Pro')  # 给name属性赋值

# 5. getattr 获取属性
print(getattr(g, 'name'))


# 6.**kw 可变参数
class Person(object):
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)


p = Person(name='言曌', age=18, sex='男')
print(p.name, p.age, p.sex)

# 7.format 字符串格式化
print('name={}, age={}'.format('言曌', 18))

# 8. len 获得列表长度
list = [1, 2, 3]
print(len(list))

# 9. str 转成字符串
num = 3.14
print(num, str(num), str(list))


# 10. 重写 __str__
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return 'name: {}, age: {}'.format(self.name, self.age)


p2 = Person2('言曌', 18)
#  print 底层调用的 __str__方法
print(p2)  # 如果不重写 __str__，默认打印 <__main__.Person2...>


# 11. __slots__ 设置限制属性，不允许动态添加或访问其他属性
class Person3:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


p3 = Person3('言曌', 18)


# p3.sex = '男' 会报错，p2.sex = '男' 不会报错

# 12. __call__ 把一个实例也变成一个可调用对象
class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, name):
        print('你好啊！ {}'.format(self.name))


p4 = Person4('言曌', 18)
p4('张三')  # 相当于p4.__call__('张三')的缩写

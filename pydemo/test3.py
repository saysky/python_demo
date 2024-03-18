# Python 3.7.4
class Person:
    # 初始化方法，类似java的构造方法，给属性赋初始值
    def __init__(self, name, age):
        self.__name = name # 私有方法，调用 p.name或p.__name会报错
        self.__age = age
    @staticmethod
    def sayHello():
        print('Hello!!!')

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


# 1.调用类方法
Person.sayHello()

# 2.创建实例
p = Person("言曌", 18)

# 调用实例方法
print(p.getName())

p.setName("言曌GG")
print(p.getName())
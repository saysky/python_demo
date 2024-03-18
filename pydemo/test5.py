# Python 3.7.4
class Person:
    # 类属性定义，类似于java的static属性
    MAX_AGE = 150  # 最大年龄，150岁。公开属性，类似java的public权限，可以直接读取和修改
    __MAX_HEIGHT = 250  # 最大身高，250cm。私有属性以__开头，类似java的private权限，对外访问需要提供公开方法

    # 定义类方法，私有方法对外访问需要提供公开方法
    @classmethod  # 只有类方法需要加这个注解
    def get_MAX_HEIGHT(cls):
        return cls.__MAX_HEIGHT

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print('Hello', self.name)


# 党员
class DangYuan(Person):

    def __init__(self, name, age, joinDate):
        super().__init__(name, age)
        self.joinDate = joinDate  # 入党日期

    def sayHello(self):
        print('我爱党，我的入党日期是：', self.joinDate)


p = DangYuan('小明', 18, '2024-1-1')
print(p.name, p.age, p.joinDate)  # 可以访问(读写)父类的属性
p.sayHello()  # 优先调用本类的方法，本类没有再去调用父类的

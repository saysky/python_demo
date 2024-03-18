# Python 3.7.4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print('Hello', self.name)


# 党员，核心信息
class DangYuan(Person):

    def __init__(self, name, age, joinDate):
        super().__init__(name, age)
        self.joinDate = joinDate  # 入党日期

    def sayHello(self):
        print('我爱党，我的入党日期是：', self.joinDate)


# 党员信息详情，其他信息
class DangYuanDetails(DangYuan):

    def __init__(self, name, age, joinDate, introducer):
        super().__init__(name, age, joinDate)
        self.introducer = introducer  # 介绍人


p = DangYuanDetails('张三', 18, '2023-1-1', '李四')
print(p.name, p.age, p.joinDate, p.introducer)
p.sayHello()

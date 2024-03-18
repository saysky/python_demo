# Python 3.7.4
# class Person:
#     # 初始化方法，类似java的构造方法，什么都不做
#     def __init__(self): pass
#
#
# # 创建实例，并赋值，不需要事先定义这个属性
# p = Person()
# p.age = 18
# print(p.age)


# class Person:
#     # 初始化方法，类似java的构造方法，给属性赋初始值
#     def __init__(self):
#         self.age = 18
#         self.country = 'China'
#
#
# # 创建实例，并赋值，不需要事先定义这个属性
# p = Person()
# print(p.age, p.country)  #
# # 提示：如果访问未赋值的属性会报错，如 p.name

class Person:
    # 初始化方法，类似java的构造方法，给属性赋初始值
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建实例，并赋值，不需要事先定义这个属性
p = Person("张三", 18)
print(p.name, p.age)
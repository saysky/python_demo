# Python 3.7.4
# 定义Person类，继承于object类
class Person:
    # 类属性定义，类似于java的static属性
    MAX_AGE = 150  # 最大年龄，150岁。公开属性，类似java的public权限，可以直接读取和修改
    __MAX_HEIGHT = 250  # 最大身高，250cm。私有属性以__开头，类似java的private权限，对外访问需要提供公开方法

    # 定义类方法，私有方法对外访问需要提供公开方法
    @classmethod  # 只有类方法需要加这个注解
    def get_MAX_HEIGHT(cls):
        return cls.__MAX_HEIGHT


print(Person.MAX_AGE)
print(Person.get_MAX_HEIGHT())

Person.MAX_AGE = 120  # 可以直接修改

# 也可以创建对象来访问类型属性，java不支持
p = Person
print(p.MAX_AGE)

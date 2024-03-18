# Python 3.7.4
class Goods:  # 商品类
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sayHello(self):
        print('Hello', self.name, self.price)


class Author:  # 作者类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print('Hello', self.name, self.age)


class Book(Goods, Author):  # 书籍类，同时继承2个父类
    def __init__(self, goodsName, goodsPrice, authorName, authorAge, publisher):
        # 多个父类时
        Goods.__init__(self, goodsName, goodsPrice)  # 父类，商品的属性
        Author.__init__(self, authorName, authorAge)  # 父类，作者的属性
        self.publisher = publisher  # 书籍特有属性，出版社

    def sayHello(self):
        # 注意加载顺序，name因为存在同名，先被赋值为“一本好书”，后被覆盖为“张三”
        print('Hello', self.name, self.age, self.publisher, self.price)


b = Book('一本好书', 18.8, '张三', 18, '武当出版社')
print(b.age)
b.sayHello()

# for循环
sum = 0
for item in range(1, 100):
    sum += item
print(sum)

# input输入值
x = input("请输入1个数：")
y = input("请输入1个数：")

print("{}+{}={}".format(x, y, int(x) + int(y)))

# 一次性读入多个
str = input("请输入2个数，空格分隔：")
values = str.split(" ")
if len(values) == 2 and values[0].isdigit() and values[1].isdigit():
    x = values[0]
    y = values[1]
    print("{}+{}={}".format(x, y, int(x) + int(y)))

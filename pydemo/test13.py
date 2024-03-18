from urllib import request

response = request.urlopen('https://liuyanzhao.com')
print(response.url)  # URL
print(response.status)  # 状态码
for k, v in response.getheaders():  # 响应头key-value
    print('{}: {}'.format(k, v))

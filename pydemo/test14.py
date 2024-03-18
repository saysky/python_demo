# Enter a code
import requests

# 如果报错urllib3 v2.0 only supports OpenSSL 1.1.1+，可以修改urllib3由2.0改成1.26版本
# pycharm设置里，Preferences | Project: 项目名 | Python Interpreter 里 点加号，搜索urllib3，安装1.26.15
response = requests.get('https://liuyanzhao.com')
print(response, response.status_code)
print(response.headers)
content = str(response.content, 'utf-8')  # 页面内容
# print(content)


# 正则表达式，获得href里的链接
import re


def get_href_contents(html):
    # 正则表达式匹配href属性
    href_pattern = re.compile(r'href="(.*?)"')
    # 使用findall方法获取所有匹配项
    href_contents = href_pattern.findall(html)
    return href_contents


content_list = content.split('\n')  # 分行
len(content_list)  # 打印页面内容的行数
for line in content_list:
    if 'href' in line:  # 包含href的行
        list = get_href_contents(line.strip())
        for item in list:
            print(item)

###########################
# 1. 字符串格式化
# 2. 字符串模板
#
#
###########################


# error：字符串不允许部分赋值
# website = 'http://www.baidu.com'
# website[-3:] = 'org'


# 字符串格式化
format = "Hello, %s. Is your age %d?. And you scored %.2f points"
values = ('张三', 16, 78.1234)
print(format % values)

# 模板字符串
## 常规替换
from string import Template
s = Template('$a, 哈哈哈, $a')
print(s.substitute(a='张三'))

## 不一定只能是单个字母
s = Template('$abc, 哈哈哈, $abc')
print(s.substitute(abc='张三'))

## 替换的是单词的一部分，需要括起来
s = Template('${x}yz')
print(s.substitute(x='张三'))

print("---------------------------------")

## 使用字典
s = Template('$a, $b, $c')
d = {}
d['a']='value1'
d['b']='value2'
d['c']='value3'
print(s.substitute(d))

print("---------------------------------")
# # error: 会报错
# s = Template('$a, $b, $c')
# d = {}
# d['a']='value1'
# d['b']='value2'
# print(s.substitute(d))

print("---------------------------------")
# 不会报错
s = Template('$a, $b, $c')
d = {}
d['a']='value1'
d['b']='value2'
print(s.safe_substitute(d))
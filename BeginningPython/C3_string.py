# #coding=UTF-8
'''
1. 字符串格式化
2. 字符串模板
'''
from turtledemo.penrose import makeshapes

# error：字符串不允许部分赋值
# website = 'http://www.baidu.com'
# website[-3:] = 'org'

# 字符串格式化
format = "Hello, %s. Is your age %d?. And you scored %.2f points"
values = ('张三', 16, 78.1234)
print(format % values)

# 模板字符串
# # 常规替换
from string import Template
s = Template('$a, 哈哈哈, $a')
print(s.substitute(a='张三'))

# # 不一定只能是单个字母
s = Template('$abc, 哈哈哈, $abc')
print(s.substitute(abc='张三'))

# # 替换的是单词的一部分，需要括起来
s = Template('${x}yz')
print(s.substitute(x='张三'))

print("---------------------------------")

# # 使用字典
s = Template('$a, $b, $c')
d = {}
d['a'] = 'value1'
d['b'] = 'value2'
d['c'] = 'value3'
print(s.substitute(d))

print("---------------------------------")
# # error: 会报错
# s = Template('$a, $b, $c')
# d = {}
# d['a']='value1'
# d['b']='value2'
# print(s.substitute(d))

print("---------------------------------")
# safe_substitute()不会报错
s = Template('$a, $b, $c')
d = {}
d['a'] = 'value1'
d['b'] = 'value2'
print(s.safe_substitute(d))

print("---------------------------------")
# 字符串常量
import string
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable)
print(string.punctuation)

print("-------------find 方法--------------------")

print("abcedfg123hi".find('ce'))
print("abcedfg123hi".find('de'))
print("$$$ money $$$$".find('$$$'))  # 返回的不是boolean值，0代表有值，位置为0而已

# find方法还可指定起始和终止位置
print("$$$ money $$$$".find('$$$', 1))  # 不会返回0

# 找不到，会返回-1;按照python惯例，包含1，不包含11
print("$$$ money $$$$".find('$$$', 1, 11))  

print("-------------join() 方法--------------------")
# split的逆方法，添加间隔符
a = ['a', 'b', 'c']
print("".join(a))  # abc
print("/".join(a))  # a/b/c

print("a".join("b"))  # 结果是b，因为没地方可添加

a = ('1', '2', '3')
print("a".join(a))  # 元组也可以join
a = '1', '2', '3'
print("a".join(a))  # 逗号分隔，自动视为元组
'''
a = (1,2,3)
print("a".join(a)) # expected str instance, int found，不能join数字
'''

print("-------------lower() 方法--------------------")
name = 'Mike'
names = ['mike', 'kate']
if(name in names): print ('name in names 1')
if(name.lower() in names): print ('name in names 2')

print("-------------replace() 方法--------------------")
print('This is a desk'.replace('is', 'is_'));  # 会替换所有的is

print("-------------split() 方法--------------------")
# 如果不加任何参数，以分隔符（包括空格、换行、制表）为分隔符
a = 'a    b c'
print(a.split());  # 会替换所有的is

print("-------------strip() 方法--------------------")
a = ' a b c    ';
print("|" + a.strip() + "|");
a = '#abc$'
print("|" + a.strip('#$') + "|"); #参数指定的顶部和尾部的所有字符都会被去除
a = '##abc$'
print("|" + a.strip('#$') + "|"); #会循环去除，直至收尾字符不在参数中
a = '## abc$'
print("|" + a.strip('#$ ') + "|"); #会循环去除，直至收尾字符不在参数中，空格直接输入即可
print("|" + a.lstrip('#$ ') + "|"); #左去除
print("|" + a.rstrip('#$ ') + "|"); #右去除

print("-------------translate() 方法--------------------")
table = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456'
a = 'abcdef'.translate(table)
print(a)

## 未完待续
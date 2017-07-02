# coding=UTF-8
'''
条件、循环和其他语句

'''
print("--------------print语句-------------------")
# print要打印多个变量，直接用逗号隔开即可，打印结果以空格隔开
# Python3.0中不再支持print 1,2,3的写法，不再是语句，变成函数
print(1, 2, 3)

# 不采用格式化字符串的方法打印
name = 'Tom'
hello = '中午好'
print(name + ',', hello + '!')

print("--------------import语句-------------------")

# import语句
import string
from string import capwords
from string import Template, capwords
from string import *  # 只有确定要引入模块所有功能时，才使用最后一种方式

# 如果两个包中有同名函数，可以指定别名
import string as s1  # 给模块指定别名
from string import capwords as c1  # 给方法指定别名
x = capwords('thsi fda fda')
print(x)
x = c1('ha ha f')
print(x)
x = s1.capwords('a b cd efg');
print(x)

print("--------------赋值魔法-------------------")
#批量复制
x, y, z = 1, 2, 3
print(x, y, z)
#交换变量
x, y = y, x
print(x, y) # 注意，同时进行，并不是先x=y, 然后y=x

#当函数或者方法返回元组（或者其他序列或可迭代对象时），该特性尤其有用
aa = {'name':'Tom', 'age':13}
a1, a2 = aa #这种写法，长度必须刚好是2
# a1, a2, a3 = aa #ValueError: not enough values to unpack (expected 3, got 2)
print(a1,'/',a2) #结果： name / age，显示两个内容的key
a1, a2 = aa.popitem()
print(a1,'/',a2)
a1, a2 = aa.popitem()
print(a1,'/',a2)
# a1, value = aa.popitem() # KeyError: 'popitem(): dictionary is empty'

print("--------------星号赋值-------------------")
b1, b2, *b3 = {1,2,3,4,5,6} # 右侧的赋值语句需要是可迭代对象
print(b1, b2, b3) #1 2 [3, 4, 5, 6]， b3的结果是序列 

print("--------------链式赋值-------------------")
'''
x = y = somefunction()
等同于 
y = somefunction()
x = y
不一定等同于
y = somefunction()
x = somefunction()
'''
print("--------------缩排-------------------")





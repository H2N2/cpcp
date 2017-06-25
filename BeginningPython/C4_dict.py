# coding=UTF-8
'''
字典

'''
from pip._vendor.distlib.compat import raw_input
from copy import _deepcopy_atomic
print("--------------字典的定义-------------------")
tels = {'Mike':'1142', 'Kate':'4112'}
tels = {}  # 定义空字典

print("--------------dict()  函数-------------------")
items = [('name', 'Mike'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])

# 会抛异常
# d = dict(('name', 'Tom'))

d = dict(name='Kate', age=22)
print(d)

c = dict(d);  # 也可以以映射作为函数，也可使用copy方法
print(c)

d = dict();  # 创建一个空字典
print(d)

print("--------------基本字典操作-------------------")
d = dict(name='Kate', age=22)
# 长度
print(len(d)) 
# 赋值
d['name'] = 'Tom' 
print(d)
# 删除item
del d['name']
print(d)
# 判断是否存在(以key判断)
print('name' in d)
print('age' in d)

d = dict(name='Kate', age=22)
# print(d['name1']) # 如果没有这个key，会抛异常 KeyError
d['name1'] = 'Linda'
print(d)

print("--------------电话本示例-------------------")
# 模拟一个简单的数据库
people = {
    'Alice':{
        'phone':'2341',
        'addr':'朝阳路'
    },
    'Tom':{
        'phone':'1234',
        'addr':'海淀路'
    }
}
# 描述性标签，打印输出时使用
labels = {
    'phone':'phone number',
    'addr': 'address'
}

# name = raw_input('Name: ')
name = 'Tom'
# 查询电话还是地址
# request = raw_input('Phone number (p) or address (a)?')
request = 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people : print("%s'S %s is %s." % (name, labels[key], people[name][key]))
print('The End')



print("--------------字典的格式化字符串-------------------")
phonebook = {'Tom':'1234', 'Mike':'2345'}
print("Tom's phone is %(Tom)s" % phonebook)  # 后面这个s必不可少

print("--------------字典方法 clear()-------------------")
x = {'A':1, 'B':2}
y = x
x = {}
print(y)  # 无变化

x = {'A':1, 'B':2}
y = x
x.clear()  # 原地操作，无值返回
print(y)

print("--------------字典方法 copy()-------------------")
# copy()方法时浅拷贝
x = {'a':'1', 'c':{'cc':'11'}}
y = x.copy()
y['a'] = 'a1'  # x不变，仅y改变
print(x)
print(y)
y['c']['cc'] = '22'  # x、y都改变
print(x) 
print(y)
y['c'] = '3'  # x不变，仅y改变
print(x)
print(y)

print("--------------深拷贝 deepcopy()-------------------")
# 深拷贝
from copy import deepcopy
x = {'a':'1', 'c':{'cc':'11'}}
y = deepcopy(x)
y['c']['cc'] = '22'
print(x)
print(y)

print("--------------字典方法  fromkeys()-------------------")
# 使用给定的键建立新的字典
x = {}.fromkeys(['aaa', 'bbb']); 
print(x)  # 结果：{'aaa': None, 'bbb': None}
x = dict.fromkeys(['keya', 'kyeb'], 'default') 
print(x)  # 结果：{'keya': 'default', 'kyeb': 'default'}

print("--------------字典方法  get()-------------------")
# 更宽松的访问字典的方法,key不存在时不会报错
# get方法还可以设定key不存在时的默认值
d = {}
print(d.get('a'))
print(d.get('a', 'default'))

print("--------------字典方法  items()和iteritems()-------------------")
# 把字典所有的项以列表的方式返回，列表中每一项均为键值对
x = {'key1':'value1', 'key2':'value2'}
items = x.items()
print(items)
itx = x.iteritems();
print(itx)

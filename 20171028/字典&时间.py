'''字典简介

  字典(dic dictionary)是除列表之外python中最灵活的内置数据结构类型。 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
'''


'''



每个键与值必须用冒号隔开(:)，每对用逗号分割，整体放在花括号中({})。键必须独一无二，但值则不必；值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。

'''

#字典由键和对应的值组成。字典也被称作关联数组或哈希表。基本语法如下：

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

print(dict)
print(str(dict))
print(dict.items())
print(len(dict))

del dict['Alice']; # 删除键是'name'的条目
print(dict)
dict.clear()
print(dict.keys())



dict = {'name': 'Zara', 'age': 7, 'class': 'First'};
dict["age"]=27; #修改已有键的值
dict["school"]="wutong"; #增加新的键/值对
print ("dict['age']: ", dict['age'])
print ("dict['school']: ", dict['school'])
'''

cmp(dict1, dict2) #比较两个字典元素。
len(dict) #计算字典元素个数，即键的总数。
str(dict) #输出字典可打印的字符串表示。
type(variable) #返回输入的变量类型，如果变量是字典就返回字典类型。
clear() #删除字典内所有元素
copy() #返回一个字典的浅复制
fromkeys() #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
get(key, default=None) #返回指定键的值，如果值不在字典中返回default值
has_key(key) #如果键在字典dict里返回true，否则返回false
items() #以列表返回可遍历的(键, 值) 元组数组
keys() #以列表返回一个字典所有的键
setdefault(key, default=None) #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
update(dict2) #把字典dict2的键/值对更新到dict里
values() #以列表返回字典中的所有值

'''

print("--------------------------日期和时间")
import time,datetime
localtime = time.localtime(time.time())
print(localtime)

print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.strftime(datetime.datetime.now()),'%Y-%m-%d %H:%M:%S')

oneday = datetime.timedelta(days=1)
#今天，2014-03-21
today = datetime.date.today()
#昨天，2014-03-20
yesterday = datetime.date.today() - oneday
#明天，2014-03-22
tomorrow = datetime.date.today() + oneday
#获取今天零点的时间，2014-03-21 00:00:00
today_zero_time=datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
#0:00:00.001000
print (datetime.timedelta(milliseconds=1)), #1毫秒
#0:00:01
print (datetime.timedelta(seconds=1)), #1秒
#0:01:00
print (datetime.timedelta(minutes=1)), #1分钟
#1:00:00
print (datetime.timedelta(hours=1)), #1小时
#1 day, 0:00:00
print (datetime.timedelta(days=1)), #1天
#7 days, 0:00:00
print (datetime.timedelta(weeks=1))

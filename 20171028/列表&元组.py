
list=['physics', 'chemistry', 1997, 2000];

print(list[0])

list[0]="ljq"
print(list[0])
list.remove(1997)
print(list[2])
del list[1]
print(list[0:])

# list.append(obj) #在列表末尾添加新的对象
# list.count(obj) #统计某个元素在列表中出现的次数
# list.extend(seq) #在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# list.index(obj) #从列表中找出某个值第一个匹配项的索引位置，索引从0开始
# list.insert(index, obj) #将对象插入列表
# list.pop(obj=list[-1]) #移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
# list.remove(obj) #移除列表中某个值的第一个匹配项
# list.reverse() #反向列表中元素，倒转
# list.sort([func]) #对原列表进行排序1

'''
 Python的元组与列表类似，不同之处在于元组的元素不能修改；元组使用小括号()，列表使用方括号[]；元组创建很简单，只需要在括号中添加元素，并使用逗号(,)隔开即可，

'''
tup1 = ('physics', 'chemistry', 1997, 2000);
print(tup1)


print(len(tup1))

print((1,2,3)+(4,5,6))

print(3 in (1,2,3))

for x in (1,2,3):
    print(x)

'''
cmp(tuple1, tuple2) 比较两个元组元素。
len(tuple) 计算元组元素个数。
max(tuple) 返回元组中元素最大值。
min(tuple) 返回元组中元素最小值。
tuple(seq) 将列表转换为元组。
'''

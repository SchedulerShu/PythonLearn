'''
在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如 numbers = [10, 29, 30, 41]，
要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
'''

#第一种方式是通过获取列表长度来迭代列表下标
numbers = [10,29,30,41]

for i in range(len(numbers)):
    print('({0},{1})'.format(i,numbers[i]))


# 第二种方法是直接使用enumerate函数：

#内置函数 enumerate 还可以接收一个默认参数 start ，用于指定 index 从哪个数开始，默认是0，
for index ,value in enumerate(numbers):
    print(index,value)

for i in list(enumerate(numbers)):
    print(i,end=' ')


from functools import reduce
##reduce
'''
    官方解释如下： 
    
    Apply function of two arguments cumulatively to the items of sequence, from left to right, so as to reduce the sequence to a single value. 
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
    The left argument, x, is the accumulated value and the right argument, y, is the update value from the sequence. 
    If the optional initializer is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty. 
    If initializer is not given and sequence contains only one item, the first item is returned. 
    
    格式： reduce (func, seq[, init()]) 
    reduce()函数即为化简函数，它的执行过程为：每一次迭代，都将上一次的迭代结果（注：第一次为init元素，如果没有指定init则为seq的第一个元素）与下一个元素一同传入二元func函数中去执行。
    在reduce()函数中，init是可选的，如果指定，则作为第一次迭代的第一个元素使用，如果没有指定，就取seq中的第一个元素。

'''


def statistics(lst):
  dic = {}
  for k in lst:
    if not k in dic:
      dic[k] = 1
    else:
      dic[k] +=1
  return dic
lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]

print(statistics(lst))


def statistics2(lst):
  m = set(lst)
  dic = {}
  for x in m:
    dic[x] = lst.count(x)
  return dic
lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
print (statistics2(lst))


def statistics(dic,k):
  if not k in dic:
    dic[k] = 1
  else:
    dic[k] +=1
  return dic
lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
print (reduce(statistics,lst,{}))

#提供第三个参数，第一次，初始字典为空，作为statistics的第一个参数，然后遍历lst,作为第二个参数，然后将返回的字典集合作为下一次的第一个参数
#或者 d = {} d.extend(lst)
#print reduce(statistics,d)
#不提供第三个参数，但是要在保证集合的第一个元素是一个字典对象，作为statistics的第一个参数，遍历集合依次作为第二个参数


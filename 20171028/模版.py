'''
string 提供了一个灵活多变的模版类 Template ，使用它最终用户可以用简单的进行编辑。这使用户可以在不进行改变的情况下定制他们的应用程序。

格式使用 $ 为开头的 Python 合法标识（数字、字母和下划线）作为占位符。占位符外面的大括号使它可以和其它的字符不加空格混在一起。 $$ 创建一个单独的 $:
'''


from string import Template
t = Template('${village}folk send $$10 to $cause.')
t = t.substitute(village='Nottingham', cause='the ditch fund')

print(t)  #Nottinghamfolk send $10 to the ditch fund.

'''
当一个占位符在字典或关键字参数中没有被提供时，substitute() 方法就会抛出一个 KeyError 异常。 
对于邮件合并风格的应用程序，用户提供的数据可能并不完整，这时使用 safe_substitute() 方法可能
更适合 — 如果数据不完整，它就不会改变占位符:

'''

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# t = t.substitute(d,owner="sajkdklakl")
t = t.safe_substitute(d)

print(t)

'''
模板子类可以指定一个自定义分隔符。例如，图像查看器的批量重命名工具可能选择使用百分号作为占位符，像当前日期，图片序列号或文件格式:
'''

import time, os.path

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
     delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
   base, ext = os.path.splitext(filename)
   newname = t.substitute(d=date, n=i, f=ext)
print('{0} --> {1}'.format(filename, newname))



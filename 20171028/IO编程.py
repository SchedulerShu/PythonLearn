# -*- coding:utf8 -*-
import codecs



#文件读写

'''
读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
或者把数据写入这个文件对象（写文件）。


'''
#读文件

#要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

f = open('ex1.py', 'r',encoding="utf8")
# print(f.read())


#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
#     f = open('ex1.py', 'r', encoding="utf8")
#     print(f.read())
# finally:
#     f.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
#和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# with open('ex1.py', 'r', encoding="utf8") as f:
#      print(f.read())

'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取
size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
'''
# for line in f.readlines():
#     print(line.strip())

# for line in f.read(200):
#     print(line)







print("----------------------------------------写文件----------------------------------")

#文件不存在自动创建
# f = open('test.txt', 'w')
# f.write('Hello, world!')
# f.close()

with open('test.txt','w') as f:
    f.write("shufufu")



'''
UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 412: illegal multibyte sequence
    f = open('ex1.py', 'r',encoding="utf8")
    
'''


import os
#应该用 import os 风格而非 from os import *。这样可以保证随操作系统不同而有所变化的
#os 模块提供了很多与操作系统交互的函数:
print(os.get_exec_path())

print(os.getcwd())
print(os.get_exec_path())
print(dir(os))
# print(help(os))


#针对日常的文件和目录管理任务，shutil 模块提供了一个易于使用的高级接口:
import shutil
# shutil.copy(src,des)
# shutil.move(src,des)

#glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob
print(glob.glob('*.py'))


import sys
print(sys.argv)



#math 模块为浮点运算提供了对底层C函数库的访问:
import math

print(math.acos(math.pi/4.0))
print(math.log(1024,2))


#random 提供了生成随机数的工具:
import random
print(random.choice(["sajdja","u8idoaod","dsakla;dl;k"]))
print(random.random())
print(random.randrange(1,10))


# 数据压缩
#以下模块直接支持通用的数据打包和压缩格式：zlib， gzip， bz2， lzma， zipfile 以及 tarfile。

import zlib

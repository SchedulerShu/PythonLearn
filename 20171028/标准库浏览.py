import reprlib
'''
reprlib 模块为大型的或深度嵌套的容器缩写显示提供了 :repr() 函数的一个定制版本:
'''
print(reprlib.repr(set('supercalifragilisticexpialidocious')))


import pprint
'''
    pprint 模块给老手提供了一种解释器可读的方式深入控制内置和用户自定义对象的打印。当输出超过一行的时候，
    “美化打印（pretty printer）”添加断行和标识符，使得数据结构显示的更清晰:
'''
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
print(pprint.pprint(t,width=30))



#textwrap 模块格式化文本段落以适应设定的屏宽:
import textwrap
doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
     the wrapped lines."""

print(textwrap.fill(doc,width=40))


'''
locale 模块按访问预定好的国家信息数据库。locale 的格式化函数属性集提供了一个直接方式以分组标示格式化数字:
'''
import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

print(locale.localeconv())

x = 1234567.8
print(locale.format('%f',x,grouping=True))


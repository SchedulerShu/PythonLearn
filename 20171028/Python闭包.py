

'''
内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变
'''


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = [ ]
    for i in range(1, 4):
        print(i)
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print (f1(), f2(), f3())



def count():
    fs = []
    for i in range(1, 4):
        print(i)
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print (f1(), f2(), f3())

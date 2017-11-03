'''
定义一个类时，大家用得最多的就是 __init__ 方法，而 __new__ 和 __call__ 使用得比较少，这篇文章试图帮助大家把这3个方法的正确使用方式和应用场景分别解释一下。

关于 Python 新式类和老式类在这篇文章不做过多讨论，因为老式类是 Python2 中的概念，现在基本没人再会去用老式类，新式类必须显示地继承 object，而 Python3 中，
只有新式类，默认继承了 object，无需显示指定，本文代码都是基于 Python3 来讨论。

'''
#__init__方法:

#__init__方法负责对象的初始化，系统执行该方法前，其实该对象已经存在了，要不然初始化什么东西呢？先看例子：

# class A(object): python2 必须显示地继承object
class A:
    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        return super(A, cls).__new__(cls)

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

A()

'''
从输出结果来看， __new__方法先被调用，返回一个实例对象，接着 __init__ 被调用。 __call__方法并没有被调用，这个我们放到最后说，
先来说说前面两个方法，稍微改写成：
'''
class B:
    def __init__(self):
        print("__init__ ")
        print(self)
        super(B, self).__init__()

    def __new__(cls):
        print("__new__ ")
        self = super(B, cls).__new__(cls)
        print(self)
        return self

B()

class C:
    def __init__(self,*args,**kwargs):
        print("init",args,kwargs)

    def __new__(cls, *args, **kwargs):
        print("new",args,kwargs)
        return super().__new__(cls)

C(1,2,3)

print("-------------------------------------__new__方法-------------------------------------")
#__new__ 方法

'''
一般我们不会去重写该方法，除非你确切知道怎么做，什么时候你会去关心它呢，它作为构造函数用于创建对象，是一个工厂函数，
专用于生产实例对象。著名的设计模式之一，单例模式，就可以通过此方法来实现。在自己写框架级的代码时，可能你会用到它，我们
也可以从开源代码中找到它的应用场景，例如微型 Web 框架 Bootle 就用到了。
'''
class BaseControllar(object):
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = object.__new__(cls,args,kwargs)
            return cls._singleton



print("-------------------------------------__call__方法-------------------------------------")

#__call__ 方法
'''
关于 __call__ 方法，不得不先提到一个概念，就是可调用对象（callable），我们平时自定义的函数、内置函数和类都属于可调用对象，
但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable
'''
#如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象，我们回到最开始的那个例子：

# a = A()
# print(callable(a))  # True

#a是实例对象，同时还是可调用对象，那么我就可以像函数一样调用它。试试：
# a()

b = B()
print(callable(b))

b()
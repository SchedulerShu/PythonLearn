# -*- coding:utf-8 -*-
import io
import re

class Counter:
    def __init__(self, path):
        """
        :param path: 文件路径
        """
        self.mapping = dict()
        with io.open(path, encoding="utf-8") as f:
            data = f.read()
            words = [s.lower() for s in re.findall("\w+", data)]
            # print(words)
            for word in words:
                self.mapping[word] = self.mapping.get(word, 0) + 1  # 函数返回指定键的值，如果存在就计算加1
                # print(self.mapping)

    def most_common(self, n):
        assert n > 0, "n should be large than 0"
        return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[:n]


if __name__ == '__main__':

    most_common_5 = Counter("test.txt").most_common(5)

    for item in most_common_5:
        print(item)


'''

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。




Python lower() 方法转换字符串中所有大写字符为小写。

lower()方法语法：
    str.lower()  //返回将字符串中所有大写字符转换为小写后生成的字符串。
'''

# str = "THIS IS STRING EXAMPLE....WOW!!!";
# print(str.lower())



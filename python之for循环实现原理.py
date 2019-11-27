
'''
for主要用于循环遍历可迭代数据对象的数据对象

list,tuple,dict,set,字符串等是内置的可迭代数据对象

判断一个对象是否是一个可迭代对象，可以使用如下方法
from collections import Iterator
isinstance('abc', Iterator)

'''
##遍历内置可迭代对象
list = ['l', 'i','s','t']
tuple = ('t', 'u','p','l','e')
dict = {'dict1':1,'dict2':2,'dict3':3,'dict4':4}
set = {'s', 'e','t'}
str = 'str'

for i in list: print(i)
for i in tuple:print(i)
for i in dict:print(i)
for i in set:print(i)
for i in str:print(i)

###多值for操作
for x,y in [(1,2), (3, 4), (5,6)]:
    print (x, y)

###生成下标

for i, l in enumerate(list):
    print(i, l)
#下标从指定值开始
for i, l in enumerate(list, 1):
    print(i, l)


###生成列表
list = []
for i in range(5):
    list.append(i)
print(list)
##更简单的生成列表的方法
list = [x*x for x in range(5)]
list = [x*x for x in range(10) if x%2 == 0]
###多个for同时判断

list = [m+n for m in range(5) for n in range(5)]

dict = {'dict1':1,'dict2':2,'dict3':3,'dict4':4}
###获取字典的键值对
for k, v in dict.items():
    print(k , v)


# 除了内置的可迭代对象之外python还支持自定义可迭代对象

# for ... in ...这个语句其实就是做了两件事
# 1.调用对象的_iter_得到对象
# 2.调用对象的_next_来进行遍历

##自定义迭代器的实现
class test():
    def __init__(self, data=1):
        self.data = data
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.data < 5:
            self.data += 1
            return self.data
        else:
            raise StopIteration

t = test()
for i in t:
    print(i) 
import sys
import Fibonacci

# from  Fibonacci import  fib2

# for i in sys.argv:
#     print(i)
#
# Fibonacci.fib(10)
# print(Fibonacci.fib2(10))
# print(dir())

#
# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),end="aaa")
#     print(repr(x * x * x).rjust(4),end="bbb")
#

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
selfref_list.append(selfref_list)

output = open('data.txt', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.txt', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
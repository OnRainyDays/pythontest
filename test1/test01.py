s = "hello 'jack'..."
print (s);
#s="hello "jack"..."
#print(s)
n = "hello \"javc\"..."
print(n);

s='''hello"jack"...'''
print(s)
s="""hello "jack"..."""
print(s)
print('''hello'jeapedu.com'!''')
print('''hello'jeapedu.com\\r\'''')

print("c:\t\temp\node\jeapedu.py")
print (r"c:\t\temp\node\jeapedu.py")

s="www.jeapedu.com"
print(s[4])
print("~~~~~~~~~~~~~循环遍历~~~~~~~~~~~~")
if 2>3:
    print (2)
else:
    print(3)

results = 72
if results >= 90:
    print("优秀")
elif results >=70:
    print("良好")
elif results >=60:
    print("及格")
else:
    print("不及格")

strings = "hello world"
for i in strings:
    print (i)

for i in range(1,100,30):
    print(i)
print("~~~~~~~~~~~~~~数组和字典~~~~~~~~~~~~~~")
shuzu = [1,2,3,'a',5]
print(shuzu)
print(shuzu[0])
print(shuzu[4])

zidian = {"username":"password",4:5,'man':'woman',1:2}
print(zidian.keys())
print(zidian.values())
print(zidian.items())

print("~~~~~~~~~~~~~~~~~~函数~~~~~~~~~")

def add(a,b):
    print(a+b)
add(4,9)
print(add(4,1))
print(add)
print(add(1,3))
print("%%%%")
def add(a,b):
    return a+b
add(3,8)
print("#")
print(add(4,5))
print("******")
def add(a=32,b=12):
    return a+b
print(add())
print(add(31,3))

print("~~~~~~~~~~~~~~~~~~类与方法~~~~~~~~~~~")

class A():
    def add(self,a,b):
        return a+b
count = A()
print(count.add(1,9))

class A:
    def add(self,a,b):
        return a+b+3
class B(A):
    def sub(self,a,b):
        return a-b
count = B()
print (count.add(4,5))

import time
print(time.ctime())

from time import ctime
print(ctime())

#from time import *
#print(ctime())
#print("休息一两秒")
#sleep(2)
#print(ctime())

import sys
sys.path.append('\model')
from model import pub
print(pub.add(3,5))

try:
    open("abc.txt",'r')
except IOError:
    print("异常了！")

try:
    print(aa)
except NameError:
    print("这是一个Name异常哈哈哈@")

try:
    open("abc.txt",'r')
    print(aa)
except Exception:
    print("所有异常")

try:
    open("abc.txt",'r')
    print(aa)
except BaseException:
    print("suoyou异常")


try:
    aa="异常测试"
    print(aad)
except BaseException as err:
    print(err)
else:
    print('没有异常')

try:
    open("dwe.txt",'r')
except BaseException as err:
    print(err)

#coding=utf-8
import time

files=open("pome.txt",'r')
strs = files.readlines()

try:
    for t in strs:
         print(t)
    time.sleep(1)
finally:
    files.close()
    print('Cleaning up ... closed the file')

filename = input('please input file name:')
if filename == 'hello':
    raise NameError('input file name error!')

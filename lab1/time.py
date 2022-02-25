from binary import binary_search
from linear import linear_search
import time
import matplotlib.pyplot as plt
import numpy
import math


t=[]
y = []
a=list(range(1000,1000000,10000))
for i in a:
    start = time.time()
    binary_search(list(range(i)), 0, i-1, -1) #worstcase of binary_search- either not in array or extreme points
    end = time.time()
    t.append([end-start])
    y.append(math.log(i,2))
print(t)
plt.plot(a, t,'.')
m,b = numpy.polyfit(a, t,1)
plt.plot(a,m*a+b,label='Worst case Binary Search')
plt.plot(a,y, label='O(logn)')
t.clear()
y.clear()
for i in a:
    start = time.time()
    binary_search(list(range(i)),0, i-1, i//2)
    end = time.time()
    t.append([end-start])
    y.append(1)
plt.plot(a, t,'.')
m,b = numpy.polyfit(a, t,1)
plt.plot(a,m*a+b,label='Best case Binary Search') #bestcase of binary_search- mid element
plt.plot(a,y, label='O(1)')
t.clear()
y.clear()
for i in a:
    start = time.time()
    linear_search(list(range(i)),0)
    end = time.time()
    t.append([end-start])
plt.plot(a, t,'.')
m,b = numpy.polyfit(a, t,1)
plt.plot(a,m*a+b,label='Best Case Linear Search') #best case of linear search - first element

t.clear()
y.clear()
for i in a:
    start = time.time()
    linear_search(list(range(i)),i+1)
    end = time.time()
    t.append([end-start])
    y.append(i)
plt.plot(a, t,'.')
m,b = numpy.polyfit(a, t,1)
plt.plot(a,m*a+b,label='Worst case Linear Search') #worst case of linear search - last element or greater
plt.plot(a,y, label='O(n)')

plt.xlabel('length of array')

plt.ylabel('time')


plt.legend()
plt.show()


 
# t.clear()
# print(t)

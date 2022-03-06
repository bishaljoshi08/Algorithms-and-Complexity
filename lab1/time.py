import time

import matplotlib.pyplot as plt

from binary import binary_search
from linear import linear_search


_, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

a = range(100, 100000, 100)

# Time Complexity for Binary Search

bt = []
for i in a:
    start = time.time()
    binary_search(range(i), 0, i-1, (i-1)//2)
    end = time.time()
    bt.append(end-start)
plt1.plot(a, bt, "+", label="Best Case")

wt = []
for i in a:
    start = time.time()
    binary_search(range(i), 0, i-1, i)
    end = time.time()
    wt.append(end-start)
plt1.plot(a, wt, ".", label="Worst Case")

plt1.set_title("Binary Search")
plt1.set_xlabel("Length of Array")
plt1.set_ylabel("Time (in secs)")
plt1.legend()

# Time Complexity for Linear Search

bt = []
for i in a:
    start = time.time()
    linear_search(range(i), 0)
    end = time.time()
    bt.append(end-start)
plt2.plot(a, bt, "+", label="Best Case")

wt = []
for i in a:
    start = time.time()
    linear_search(range(i), i)
    end = time.time()
    wt.append(end-start)
plt2.plot(a, wt, ".", label="Worst Case")

plt2.set_title("Linear Search")
plt2.set_xlabel("Length of Array")
plt2.set_ylabel("Time (in secs)")
plt2.legend()

plt.show()

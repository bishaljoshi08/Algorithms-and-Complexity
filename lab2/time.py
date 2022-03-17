import time
import matplotlib.pyplot as plt

from insertion_sort import insertion_sort
from merge_sort import merge_sort

_, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

a = range(10, 1000, 10)

bt = []
for i in a:
    start = time.time()
    insertion_sort(list(range(i)))
    end = time.time()
    bt.append((end-start)*10**6)
plt1.plot(a, bt, "+", label = "Best Case")

wt = []
for i in a:
    start = time.time()
    insertion_sort(list(reversed(range(i))))
    end = time.time()
    wt.append((end-start)*10**6)
plt1.plot(a, wt, "*", label = "Worst Case")

plt1.set_title("Insertion Sort")
plt1.set_xlabel("Length of Array")
plt1.set_ylabel("Time (in microsecs)")
plt1.legend()

bt = []
for i in a:
    start = time.time()
    merge_sort(list(range(i)), 0, len(range(i)) - 1)
    end = time.time()
    bt.append((end-start)*10**6)
plt2.plot(a, bt, "+", label = "Best Case")

wt = []
for i in a:
    start = time.time()
    merge_sort(list(reversed(range(i))), 0, len(range(i)) - 1)
    end = time.time()
    wt.append((end-start)*10**6)
plt2.plot(a, wt, "*", label = "Worst Case")

plt2.set_title("Merge Sort")
plt2.set_xlabel("Length of Array")
plt2.set_ylabel("Time (in microsecs)")
plt2.legend()

plt.show()
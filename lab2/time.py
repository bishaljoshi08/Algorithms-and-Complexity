import time
import matplotlib.pyplot as plt

from insertion_sort import insertion_sort
from merge_sort import merge_sort

_, (plt1, plt2, plt3) = plt.subplots(nrows=1, ncols=3)

a = range(10, 1000, 10)

bt = []
for i in a:
    start = time.time()
    insertion_sort(list(range(i)))
    end = time.time()
    bt.append((end-start)*10**6)
plt1.plot(a, bt, ".")

plt1.set_title("Insertion Sort(Best case)")
plt1.set_xlabel("Length of Array")
plt1.set_ylabel("Time (in microsecs)")


wt = []
for i in a:
    start = time.time()
    insertion_sort(list(reversed(range(i))))
    end = time.time()
    wt.append((end-start)*10**6)
plt2.plot(a, wt, ".")

plt2.set_title("Insertion Sort(Worst case)")
plt2.set_xlabel("Length of Array")
plt2.set_ylabel("Time (in microsecs)")

bt = []
for i in a:
    start = time.time()
    merge_sort(list(range(i)), 0, len(range(i)) - 1)
    end = time.time()
    bt.append((end-start)*10**6)
plt3.plot(a, bt, ".")


plt3.set_title("Merge Sort")
plt3.set_xlabel("Length of Array")
plt3.set_ylabel("Time (in microsecs)")

plt.tight_layout()
plt.show()
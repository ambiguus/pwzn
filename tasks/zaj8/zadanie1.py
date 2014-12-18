import pyximport; pyximport.install()
import cquickSort
import quickSort
import numpy as np
import time
import random

if __name__ == '__main__':
    n = 10
    list = random.sample(range(100),n)
    list1 = list.copy()
    start = time.monotonic()
    print(list)
    nlist = np.asarray(list, dtype=np.float64)
    cquickSort.quicksort(nlist, 0, n-1)
    print(time.monotonic() - start)
    start = time.monotonic()
    quickSort.quicksort(list1, 0, n-1)
    print(time.monotonic() - start)
    print(nlist)
    print(list1)
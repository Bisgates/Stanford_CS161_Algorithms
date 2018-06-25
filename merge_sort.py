# 2018-05-27
# Merge sort

def merge_sort(lis):
	n = len(lis)
	mid = int(n/2)
	if n <= 1:
		return lis
	C = merge_sort(lis[:mid])
	D = merge_sort(lis[mid:])
	return merge(C, D)

def merge(C, D):
	A = []
	while C != [] and D != []:
		if C[0] < D[0]:
			A.append(C.pop(0))
		else:
			A.append(D.pop(0))
	A.extend(C)
	A.extend(D)
	return A	

def quick_sort(lis):
	if len(lis) <= 1:
		return lis
	pivod = lis[int(len(lis)/2)]
	left = [ele for ele in lis if ele < pivod]
	mid = [ele for ele in lis if ele == pivod]
	right = [ele for ele in lis if ele > pivod]
	return quick_sort(left) + mid + quick_sort(right)


#-----------------TEST------------------------

import random
from time import time
from selection_sort import selection_sort
import sys

try: 
    n = int(sys.argv[1])
except:
	n = 1000

test1 = [random.randint(-12321,432523) for _ in range(n)]

t = time()
sorted1 = merge_sort(test1)
print(time() - t)

t = time()
sorted2 = sorted(test1)
print(time() - t)

t = time()
sorted3 = quick_sort(test1)
print(time() - t)

assert sorted1 == sorted2 == sorted3


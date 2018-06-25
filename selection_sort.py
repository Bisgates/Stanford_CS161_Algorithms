# 2018-5-27
# Selection_sort

def selection_sort(lis):
	lis_sorted = []
	lis = list(lis)
	while len(lis) > 0:
		min_ele = lis[0]
		for ele in lis:
			if ele <= min_ele:
				min_ele = ele
		lis_sorted.append(min_ele)
		lis.remove(min_ele)
	return lis_sorted
				

#---------------------TEST------------------------

if __name__ == "__main__":
	from time import time
	import random

	test1 = [random.randint(-10000000, 100000000) for _ in range(1000)]

	t = time()
	sorted1 = selection_sort(test1)
	print(time()-t)

	t = time()
	sorted2 = sorted(test1)
	print(time()-t)


	assert sorted1 == sorted2



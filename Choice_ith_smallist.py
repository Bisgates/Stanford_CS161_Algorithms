import random

lis = [random.randint(0,100) for i in range(100)]

def ith_smallest_ele(lis, i):
	if len(lis) < i:
		return None
	pivot = lis[0]
	left_lis = [ele for ele in lis if ele <= pivot]
	order = len(left_lis)
	if order == 0:
		return None
	elif order == i:
		return pivot
	elif order > i:
		return ith_smallest_ele(left_lis, i):
	else:
		right_lis = [ele for ele in lis if ele > pivot]
		return ith_smallest_ele(right_lis, i-order)
	

#-------------------TEST---------------------

lis_1 = [1,2,3,4,5,6]
lis_2 = [3,4,6,8,3,3,7]
lis_3 = []

assert ith_smallest_ele(lis_1, 7) == None
assert ith_smallest_ele(lis_2, 1) == 1

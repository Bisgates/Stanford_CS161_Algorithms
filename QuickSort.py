#2018-06-18
# two version of Quick sort, first version is naive impletion which need bunch of extra memory but much easyer to implement, and the other is inplace version which only need O(1) space complicity.

import random
#random.seed(12)
count = 0

def middle(A, l, r):
	if (r+l)%2 == 0:
		mid = int((l+r-1)/2)
	else:
		mid = int((l+r)/2)
	if A[l] < A[mid]:
		if A[l] > A[r-1]:
			return l
		elif A[mid] < A[r-1]:
			return mid
		else:
			return r-1
	else:
		if A[l] < A[r-1]:
			return l
		elif A[mid] < A[r-1]:
			return r-1 
		else:
			return mid

#def middle1(A, l, r):
#	if (r+l)%2 == 0:
#		mid = int((l+r-1)/2)
#	else:
#		mid = int((l+r)/2)
#	l_min = min(A[l], A[mid])
#	r_min = min(A[mid], A[r-1])
#	return A.index(max(l_min, r_min))

def ChoicePivod(A, l, r, mode='first'):
	pivod = {'first' : l,
			 'last' : r-1,
			'middle': middle(A, l, r) ,
			 'random' : random.randint(l, r-1)}
	return pivod[mode]

def QuickSort_naive(A):
	if len(A) <= 1:
		return A
	pivod = ChoicePivod(A, mode='first')
	left = [ele for ele in A if ele < A[pivod]]
	middle = [ele for ele in A if ele == A[pivod]]
	right = [ele for ele in A if ele > A[pivod]]
	return QuickSort_naive(left) + middle + QuickSort_naive(right)

def QuickSort(A, l, r):
	global count
	if l >= r:
		return None
	p = ChoicePivod(A, l, r, mode='middle')
	swap(A, l, p)
	count += r-l-1
	k = partation(A, l, r)
	QuickSort(A, l, k)
	QuickSort(A, k+1, r)

def partation(A, l, r):
	i = l+1
	for j in range(l+1, r):
		if A[j] < A[l]:
			swap(A, i, j)
			i += 1
	swap(A, l, i-1)
	return i-1

def swap(A, i, j):
	A[i], A[j] = A[j], A[i]


# --------------TEST----------------

with open('QuickSort.txt') as file:
	A = [int(ele.strip()) for ele in file]

QuickSort(A, 0, len(A))
print(count)
assert A == sorted(A)


A1 = [1,2,3]
A2 = [1]
A3 = [6,1,5,4,2,3]
A4 = [5,4,3,2,1,6]

# print(partation(A1,0,3))
#print(partation(A3,0,6))
#print(partation(A4,0,6))

#assert partation(A1, 0, 3) == 0
#print(A1)
#assert partation(A2, 0, 1) == 0
#print(A2)
#assert partation(A3, 0, 6) == 4
#print(A3)






A = [random.randint(0,100) for _ in range(10)]
A2 = list(range(500))
A3 = A2[::-1]
A4 = [1]
A5 = []

#print(QuickSort([3,2,5,2], 0, 4))
#for A in [A1, A2, A3, A4, A5]:

QuickSort(A,0,len(A))
assert A  == sorted(A), A

QuickSort(A2, 0, len(A2))
assert A2 == sorted(A2)
QuickSort(A3, 0, len(A3))
assert A3 == sorted(A3)
QuickSort(A4, 0, len(A4))
assert A4 == sorted(A4)


print('Passed all test casses!')

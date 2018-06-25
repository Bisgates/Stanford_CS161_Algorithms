# 2018-06-10
#"Counting the number of inversions in an array"
#
#This problem is related to measuring similarity between two ranked array.
#

def count_split(B, C):
	" Return the number of inbersions during the merge process"
	D = []
	count = 0
	while len(B) != 0 and len(C) != 0:
		if B[0] <= C[0]:
			D.append(B.pop(0))
		else:
			count += len(B)
			D.append(C.pop(0))
	return count, D+B+C

def count(A):
	" Return the number of inversions of A and sorted array of A "
	n = len(A)
	if n <= 1:
		return 0, A
	mid = int(n/2)
	b, B = count(A[:mid])
	c, C = count(A[mid:])
	d, D = count_split(B, C)
	return b+c+d, D

def count_inversions(A):
	" Return the number of inversions in array A"
	return count(A)[0]


# ---------------------TEST------------------------

with open('IntegerArray.txt') as file:
	A = [int(line.strip()) for line in file]

print(count_inversions(A))

assert count_inversions([1,3,5,2,4,6]) == 3
assert count_inversions([6,5,4,3,2,1]) == 15
assert count_inversions([1,2,3,4,5,6]) == 0
assert count_inversions([1]) == 0
assert count_inversions([]) == 0


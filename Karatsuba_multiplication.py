# 2018-5-24
# Karatsuba Algorithm, return the product of x and y


import sys
import time
from gao import kar_multiply

def kara_multiply(x, y) -> int:
	if len(x) == len(y) == 1:
		return int(x)*int(y)
	x, y = pre_process(x, y)
	n = len(x)
	mid = int(n/2)
	a, b = x[:mid], x[mid:]
	c, d = y[:mid], y[mid:]
	p = str(int(a) + int(b))
	q = str(int(c) + int(d))
	ac = kara_multiply(a, c)
	bd = kara_multiply(b, d)
	abcd = kara_multiply(p, q) - ac - bd
	return 10**n*ac + 10**mid*abcd + bd

def pre_process(x, y):
	m = max(len(x),len(y))
	n = 1
	while n < m:
		n *= 2
	x = (n-len(x))*'0' + x
	y = (n-len(y))*'0' + y
	return x, y


x = sys.argv[1]
y = sys.argv[2]
print('\nlen(x): %d, len(y): %d'%(len(x), len(y)))

print('-------------------------------------')
t0 = time.time()
result_0 = kara_multiply(x, y)
time_0 = time.time() - t0
print('My implementation:\n\nTime: %.12fs\nResult: %d '%(time_0, result_0))

print('-------------------------------------')
x, y = int(x), int(y)
t1 = time.time()
result_1 = x * y
time_1 = time.time() - t1
print('Python''s implementation: \n\nTime: %.12fs\nResult: %d'%(time_1, result_1))
		
print('-------------------------------------')
t2 = time.time()	
result_2 = kar_multiply(x, y)
print(time.time() - t2)
print(result_2)

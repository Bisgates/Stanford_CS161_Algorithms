# measure the function performance

from prettytable import PrettyTable
from time import time
import random
import sys

from QuickSort import QuickSort_naive

try:
	n = int(sys.argv[1])
except:
	n = 1000

A1 = [random.randint(-100, 10000) for _ in range(n)]
t = time()
result = QuickSort_naive(A1)






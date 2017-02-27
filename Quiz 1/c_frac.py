import sys
import timeit

def c_frac(n):
	sum = 1;
	if n == 1:
		return 2
	for i in range(n):
		sum = 1 + 1/float(sum)
	return sum

n = int(sys.argv[1])
start_time = timeit.default_timer()
print str(c_frac(n))
time = timeit.default_timer() - start_time
print str(time)
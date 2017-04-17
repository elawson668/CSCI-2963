import sys

n = int(sys.argv[1])

sum = 0

i = float(1)

while(i <= n):
	sum += 1/i
	i += 1

print sum

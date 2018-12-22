import math

q = int(input())

e = input().split()

for n in e:
	print('{:5.4f}'.format(math.sqrt(float(n))))

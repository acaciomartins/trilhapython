n = int(input())
l = input().split()

for indice in range(len(l)):
	l[indice] = int(l[indice])

print (sum(l))
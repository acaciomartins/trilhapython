x = int(input())

n = input().split()

revertido = list(n)


for i,p in enumerate(revertido):
	revertido[i] = int(p)

revertido.sort()

print (' '.join(str(x) for x in revertido))
	




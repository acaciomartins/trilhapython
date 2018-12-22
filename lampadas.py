n = int(input())
acoes = input().split()

lampadaA = 0
lampadaB = 0

for interruptor in acoes :
	
	if interruptor == '1':
		lampadaA = 1 if lampadaA == 0 else 0
	
	if interruptor == '2':
		lampadaA = 1 if lampadaA == 0 else 0
		lampadaB = 1 if lampadaB == 0 else 0

print(lampadaA)
print(lampadaB)
	

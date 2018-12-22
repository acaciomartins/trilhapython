n = int(input())
visualizacoes = []
resultado = -1
soma = 0
dia = 0

for i, elemento in enumerate(range(n)):
	visitas = int(input())
	soma = soma + visitas
	
	if soma >= 1000000 and resultado == -1:
		resultado = elemento + visitas
		dia = i + 1
		
print(dia)
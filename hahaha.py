risada = input()

vogais = ['a','e','i','o','u']

resultado = ''

for r in risada:
	if r in vogais:
		resultado += r

if resultado[::-1] == resultado:
	print ('S')
else:
	print ('N')
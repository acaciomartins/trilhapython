def eh_primo(x):

	cont_divisores = 0
	retorno = False;
	
	for divisor in range(1,x+1):
		if (x % divisor) == 0:
			cont_divisores += 1 

	if cont_divisores == 2:
		retorno = True
	
	return retorno
		
		
x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')
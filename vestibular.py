n = input()

gabarito = input()
questoes = input()

total = 0

for g, q in zip(gabarito, questoes):
	if g == q:
		total += 1

print(total)
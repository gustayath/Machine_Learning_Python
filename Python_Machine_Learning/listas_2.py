import random

''' Mostra uma das cidades de forma aleatória '''
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
escolhida = random.choice(cidades)
print(f"A cidade escolhida foi: {escolhida}.")

''' Adciona mais um índice na lista '''
a = [1, 2, 3]
a.append(4)
print(a)

''' Adciona mais valores a lista da variável "a" '''
b = [10, 20, 30]
for i in b:
    a.append(i)

print(a)

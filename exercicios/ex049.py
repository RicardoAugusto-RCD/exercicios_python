
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que utilizando o laço for.

n = int(input('Digite um número e descubra sua tabuada: '))

for c in range(0, 11):
    print('=-' * 7)
    print('{} x  {} = {}'.format(n, c, n*c))


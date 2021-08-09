
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram → ', end='')

for numero in aleatorio:
    print(f'{numero}', end=' ')

maior = max(aleatorio)
print(f'\nO maior valor foi → {maior}')

menor = min(aleatorio)
print(f'O menor valor foi → {menor}')

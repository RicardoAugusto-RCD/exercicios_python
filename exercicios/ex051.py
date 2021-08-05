
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

primeiro = int(input('Primeiro termo: '))

razao = int(input('Razão: '))

ultimo = primeiro + (10 - 1) * razao

for c in range(primeiro, ultimo, razao):

    print('{} -> '.format(c), end='')

else:
    print(ultimo)

# Crie um programa que leia o ano do nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for c in range(1, 8):

    anoNascimento = int(input('{}º ano de nascimento: '.format(c)))

    calculoIdade = date.today().year - anoNascimento

    if calculoIdade >= 18:
        maior = maior + 1

    elif calculoIdade < 18:
        menor = menor + 1

print('Maiores: {}'.format(maior))
print('Menores: {}'.format(menor))
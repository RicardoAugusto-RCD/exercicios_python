
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM.
# Até 14 anos: INFANTIL.
# Até 19 anos: JUNIOR.
# Até 25 anos: SÊNIOR.
# Acima: MASTER.

from datetime import date

anoAtual = date.today().year

anoNascimento = int(input('Digite o ano do nascimento: '))

idade = anoAtual - anoNascimento

print('Atleta com {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: Mirim.')

elif idade <= 14:
    print('Categoria: Infantil.')

elif idade <= 19:
    print('Categoria: Junior.')

elif idade <= 25:
    print('Categoria: Sênior.')

else:
    print('Categoria: Master.')


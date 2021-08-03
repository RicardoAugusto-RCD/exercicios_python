
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))

numero2 = int(input('Digite outro número: '))

numero3 = int(input('Digite mais um número: '))

if numero1 > numero2 and numero1 > numero3:
    print('Maior {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('Maior {}'.format(numero2))
elif numero3 > numero1 and numero3 > numero2:
    print('Maior {}'.format(numero3))
else:
    print('Iguais')

if numero1 < numero2 and numero1 < numero3:
    print('Menor {}'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('Menor {}'.format(numero2))
elif numero3 < numero1 and numero3 < numero2:
    print('Menor {}'.format(numero3))
else:
    print('Iguais')

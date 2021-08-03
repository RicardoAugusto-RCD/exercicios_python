
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Ímpar.

numero = int(input('Digite um número inteiro: '))

resto = numero % 2

if resto == 0:
    print('Par')

else:
    print('Impar')

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção Inteira.

from math import trunc

num = float(input("Digite um número qualquer: "))

print('A porção Inteira do número {} é {}.\n'.format(num, trunc(num)))

#ou

print('A porção Inteira do número {} é {}.'.format(num, int(num)))



# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

n = 0
c = 0
s = 0
m = 0
continuar = ''

while continuar != 'N':

    n = int(input('Digite um número: '))

    if continuar == 'S':
        s += n
        c += 1
        m = s / c
        

    continuar = str(input('Deseja continuar? ')).upper().strip()

print('Média {}'.format(m))







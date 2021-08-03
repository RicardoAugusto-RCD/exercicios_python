
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numeroPc = random.randint(0,5)

numeroUsuario = int(input('Digite um número entre 0 e 5: '))

if numeroUsuario == numeroPc:
    print('O computador "pensou" no número {} e você acertou!!!'.format(numeroPc))
else:
    print('O computador "pensou" no número {} e você errou!!!'.format(numeroPc))

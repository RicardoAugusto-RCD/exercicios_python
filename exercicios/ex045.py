
# Crie um programa que faça o computador jogar Jokenpô com você.

import random

computador =  random.randint(1,3)

usuario = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite sua escolha: '))

if usuario == 1 and computador == 1 or usuario == 2 and computador == 2 or usuario ==  3 and computador == 3:
    print('Empate!!!')
elif usuario == 1 and computador == 2 or usuario == 2 and computador == 3 or usuario == 3 and computador == 1:
    print('Você Perdeu, o Computador Ganhou!!!')
else:
    print('Você Ganhou do Computador!!!')



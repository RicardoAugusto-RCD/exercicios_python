
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if jogador == 0 or jogador == 1 or jogador == 2:

    print('=' * 45)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print(('=' * 45))

    if jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador ==  2 and computador == 2:
        print('Empate!!!')
    elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
        print('Você Perdeu, o Computador Ganhou!!!')
    elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
        print('Você Ganhou do Computador')
    print(('=' * 45))

else:
    print(('=' * 45))
    print('Jogade Inválida, tente outra vez')
    print(('=' * 45))



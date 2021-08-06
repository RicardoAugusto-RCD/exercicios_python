
# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

numeroUsuario = int(input('Digite um número entre 0 e 10: '))

numeroPc = random.randint(0,10)

tentativaUsuario = 1

while numeroUsuario != numeroPc:
    print('Tente novamente!')

    numeroUsuario = int(input('Digite um número entre 0 e 10: '))

    tentativaUsuario += 1

print('O computador "pensou" no número {} e você acertou!!!'.format(numeroPc))

print('Você conseguiu acertar com {} tentativas'.format(tentativaUsuario))

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogada = dict()
contador = 1

jogada['jogador1'] = randint(1, 6)
jogada['jogador2'] = randint(1, 6)
jogada['jogador3'] = randint(1, 6)
jogada['jogador4'] = randint(1, 6)

print(F'{" ↓ VALORES SORTEADOS ↓"}')
for keys, valor in jogada.items():
    print(f'{keys} tirou {valor} no dado')
    sleep(1)

print()
print(f'{"↓ RANKING DOS JOGADORES ↓"}')
for jogador in sorted(jogada, key=jogada.get, reverse=True):

    print(f' {contador}ºlugar {jogador} com {jogada[jogador]}')
    sleep(1)
    contador += 1

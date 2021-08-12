
# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('—' * 30)
print('   JOGOS  PARA MEGA SENA')
print('—' * 30)

lista = list()
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quantidade:
    contador = 0
    while True:
        numeros = randint(0, 60)

        if numeros not in lista:
            lista.append(numeros)
            contador += 1

        if contador >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'—' * 5, f' → SORTEANDO {quantidade} JOGOS ← ', '—' * 5)

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1} → {l}')
    sleep(1)
print(f'—' * 10, f' → BOA SORTE ← ', '—' * 10)



# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['nome'] = str(input('Nome do jogador? '))
jogador['gols'] = list()
jogador['total'] = 0

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for contador in range(0, partidas):
    golPartida = int(input(f'Quantos gols na {contador + 1}ª partida? '))

    jogador['gols'].append(golPartida)
    jogador['total'] += golPartida

print('—' * 50)
print(f'{jogador}')
print('—' * 50)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('—' * 50)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for contador in range(0, partidas):
    print(f'→ Na partida {contador + 1} fez {jogador["gols"][contador]} gols')
print(f'Foi um total de {jogador["total"]} gols')


# Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

jogador = dict()
jogadorLista = list()

while True:

    jogador['nome'] = ''
    jogador['gols'] = list()
    jogador['total'] = 0

    jogador['nome'] = str(input('Nome do jogador? '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for contador in range(0, partidas):
        golPartida = int(input(f'Quantos gols na {contador + 1}ª partida? '))

        jogador['gols'].append(golPartida)
        jogador['total'] += golPartida

    jogadorLista.append(jogador.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print(' ► ERRO ◄ |Responda apenas S ou N|')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('—' * 50)
print(f'{"cod":<3}|{"nome":<15}|{"gols":<15}|{"total":<5}')
print('—' * 50)
for i, v in enumerate(jogadorLista):
    print('{:<3}|{:15}|{:15}|{:<5}'.format(i, v['nome'], '{}'.format(v['gols']), v['total']))
print('—' * 50)

while True:
    print('—' * 50)
    dadosJogador = int(input('Mostrar dados de qual jogador? [999 interrompe] '))
    print('—' * 50)
    if dadosJogador == 999:
        break
    else:
        if dadosJogador < len(jogadorLista):
            print(f'LEVANTAMENTO DO JOGADOR {jogadorLista[dadosJogador]["nome"]}')

            for c, v in enumerate(jogadorLista[dadosJogador]['gols']):
                print(f'No {c + 1}º jogo, fez {v} gols')
        else:
            print('Posição Inválida')
            continue

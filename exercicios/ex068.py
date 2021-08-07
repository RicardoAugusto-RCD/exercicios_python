
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

separador = ('─' * 50)
print(separador)
print('VAMOS JOGAR PAR OU ÍMPAR')
escolha = ("PAR", "Impar")
c = 0

while True:
    print(separador)
    jogada = int(input('Diga um valor: '))
    escolha = str(input('Digite PAR ou IMPAR: ')).upper()
    print(separador)
    computador = randint(0, 10)

    totalJogada = jogada + computador

    print('Deu PAR' if totalJogada % 2 == 0 else 'Deu Ímpar')
    if escolha == 'PAR':

        if totalJogada % 2 == 0:
            print('Ganhou.')
            c += 1
        else:
            print('Perdeu.')
            break

    if escolha == 'IMPAR':

        if totalJogada % 2 == 1:
            print('Ganhou')
            c += 1
        else:
            print('Perdeu.')
            break

print(separador)
print(f'O computador jogou {computador} e você jogou {jogada}. Total de {totalJogada}.')
print(f'Você ganhou {c} partidas consecutivas.')
print(separador)

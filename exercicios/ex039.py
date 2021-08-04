
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou o tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year

anoNascimento = int(input('Qual o ano do nascimento? '))

idade = atual - anoNascimento

if idade < 18:
    print('Vc tem {} anos.'.format(idade))
    tempoAlistamento = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(tempoAlistamento))
    anoAlistamento = atual + tempoAlistamento
    print('Seu alistamento será em {}.'.format(anoAlistamento))

elif idade == 18:
    print('Precisa se alistar esse ano.')

elif idade > 18:
    print('Vc tem {} anos.'.format(idade))
    tempoAlistamento = idade - 18
    print('Já se passaram {} anos do seu alistamento.'.format(tempoAlistamento))
    anoAlistamento = atual - tempoAlistamento
    print('Você deveria ter se alistado em {}.'.format(anoAlistamento))
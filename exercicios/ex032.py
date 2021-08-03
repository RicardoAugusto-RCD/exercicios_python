
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano e descubra se ele é BISSEXTO,\n digite 0 para descobrir o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("o ano {} é Bissexto".format(ano))
else:
    print("O ano {} não é Bissexto!".format(ano))

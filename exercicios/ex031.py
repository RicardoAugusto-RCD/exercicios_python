
# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para as viagens de até 200km e R$0,45 para viagens mais longas.

distanciaPercorrida = int(input('Digite a distância percorrida em km: '))

if distanciaPercorrida <= 200:
    passagem = distanciaPercorrida * 0.50
    print('Com a distância percorrida de {}km, você irá pagar R${:.2f}.'.format(distanciaPercorrida, passagem))
else:
    passagem = distanciaPercorrida * 0.45
    print('Com a distância percorrida de {}km, você irá pagar R${:.2f}.'.format(distanciaPercorrida, passagem))



# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

real = float(input('Digite quanto voçê possui na carteira e descubra quantos Dólares voçê conseguiria comprar: R$'))

dolar = real / 3.27

print('Com R${:.2f} que voçê possui na carteira, conseguiria comprar US${:.2f}'.format(real, dolar))
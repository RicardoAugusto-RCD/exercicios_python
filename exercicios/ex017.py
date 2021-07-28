
# Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot

catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(catOposto, catAdjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

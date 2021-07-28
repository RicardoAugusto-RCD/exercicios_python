
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo qualquer: '))

radiano = math.radians(angulo)

sen = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)

print('-' * 30)
print('Com o ângulo de {}º, temos:'.format(angulo))
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente : {:.2f}'.format(tan))
print('-' * 30)
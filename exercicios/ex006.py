
# Crie um  algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número e descubra o seu dobro, triplo e sua raiz quadrada:'))

d = n * 2
t = n * 3
rq = n ** (1/2)

print("O número digitado foi {}.\nO dobro é {}.\nO triplo é {}.\nE a sua raiz quadrada é {:.2f}.".format(n, d, t, rq))

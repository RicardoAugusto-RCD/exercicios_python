
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite uma velocidade em km/h: '))

if velocidade <= 80:
    print('Você estava dentro da velocidade correta da via!')
else:
    velocidadeAcima = velocidade - 80
    multa = velocidadeAcima * 7
    print('Você estava a {}km/h e o valor da multa será R${:.2f}'.format(velocidade, multa))


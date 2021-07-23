
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = int(input('Informe a quantidade de dias em que o carro ficou alugado:'))

kmPercorridos = float(input('Informe a quantidade de km percorridos:'))

totalPagar = (diasAlugados * 60) + (kmPercorridos * 0.15)

print('Voçê ficou com o carro alugado por {} dias e percorreu {:.2f}km, o valor a ser pago é R${:.2f}'.format(diasAlugados, kmPercorridos, totalPagar))
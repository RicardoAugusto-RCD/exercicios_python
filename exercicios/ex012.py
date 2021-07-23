
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))

precoDesconto = preco * 0.95

print('O preço do produto é R${:.2f}, com o desconto de 5% foi para R${:.2f}'.format(preco, precoDesconto))
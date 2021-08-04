
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

valorCasa = float(input('Qual o valor da casa: R$ '))

salarioComprador = float(input('Qual o seu salário: R$ '))

anosPagamento = int(input('Em quantos anos pretende pagar? '))

prestacaoMensal = valorCasa / (anosPagamento * 12)

print('Para pagar uma casa no valor de R${:.2f} em {} anos,'.format(valorCasa, anosPagamento), end='')
print(" a prestação será de R${:.2f} por mês.".format(prestacaoMensal))

if salarioComprador * 0.30 > prestacaoMensal :
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
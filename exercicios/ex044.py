
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

valorProduto = float(input('Digite o valor do produto: R$ '))

opcaoPagamento = int(input('[1] <-> À vista dinheiro/cheque\n[2] <-> À vista cartão\n[3] <-> 2x cartão\n'
                           '[4] <-> 3x ou mais no cartão\nDigite a opção de pagamento: '))

if opcaoPagamento == 1:
    valorProduto = valorProduto * 0.90
    print('Com o desconto de 10% o valor do produto sairá a R$ {:.2f}'.format(valorProduto))

elif opcaoPagamento == 2:
    valorProduto = valorProduto * 0.95
    print('Com o desconto de 5% o valor do produto sairá a R$ {:.2f}'.format(valorProduto))

elif opcaoPagamento == 3:
    valorProduto = valorProduto / 2
    print('Em 2x no cartão o valor do produto sairá a R$ {:.2f}, cada parcela'.format(valorProduto))

elif opcaoPagamento == 4:
    quantidadeParcela = int(input('Em quantas vezes você gostaria de parcelar? '))
    valorProduto = (valorProduto * 1.20) / quantidadeParcela
    print('Em {}x no cartão o valor do produto sairá a R$ {:.2f}, cada parcela'.format(quantidadeParcela, valorProduto))

else:
    print('OPÇÃO INVÁLIDA, tente novamente')

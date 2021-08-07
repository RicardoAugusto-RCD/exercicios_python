
# Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual o nome do produto mais barato.

separador = ('─' * 50)
totalCompra = maior1000 = menorPreco = 0
contadorProduto = 0
nomeMenorPreco = ' '

print(f'{" LOJA DO CUCA ":—^50}')
while True:
    nomeProduto = str(input('Nome produto: '))
    precoProduto = float(input('Preço: R$ '))

    totalCompra += precoProduto
    contadorProduto += 1

    if precoProduto > 1000:
        maior1000 += 1

    if contadorProduto == 1 or precoProduto < menorPreco:
        menorPreco = precoProduto
        nomeMenorPreco = nomeProduto
    #else:
        #if precoProduto < menorPreco:
            #menorPreco = precoProduto
            #nomeMenorPreco = nomeProduto

    print(separador)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print(separador)

print(f'{" PROGRAMA ENCERRADO ":—^50}')
print(f'O total da compra foi R${totalCompra:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenorPreco} que custa R${menorPreco:.2f}')
print(separador)

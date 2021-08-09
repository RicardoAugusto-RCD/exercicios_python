
# Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

produtos = ('Mouse', 150.0, 'Teclado', 200.0, 'Monitor', 1500.0, 'PlacaVídeo', 5000.0, 'Desktop', 6800.0, 'CadeiraGamer'
            , 1200.0, )

print('—' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('—' * 50)

for ordem, listaProdutos in enumerate(produtos):

    if ordem % 2 == 0:
        print(f'{listaProdutos:.<40}', end='')
    else:
        print(f'R${listaProdutos:>8.2f}')

print('—' * 50)


# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = list()
print('—' * 50)

while True:

    valor = int(input('Digite um valor: '))

    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado')
    else:
        print('Valor duplicado')
        print('—' * 50)
        continue

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break
    print('—' * 50)

print('—' * 50)
lista.sort()
print(f'Os valores únicos digitados em ordem crescente {lista}')

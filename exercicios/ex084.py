
# Faça um programa que leia nome e peso de várias pessoa, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoa foram cadastradas.
# b) Uma listagem com as pessoa mais pesadas.
# c) Uma listagem com as pessoa mais leves.

cadastros = maiorPeso = menorPeso = 0
nomeMaisPesado = []
nomeMaisLeve = []

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    cadastros += 1

    if cadastros == 1:
        maiorPeso = peso
        menorPeso = peso
        nomeMaisPesado.append(nome)
        nomeMaisLeve.append(nome)
    else:
        if peso > maiorPeso:
            maiorPeso = peso
            nomeMaisPesado.clear()
            nomeMaisPesado.append(nome)
        if peso == maiorPeso:
            nomeMaisPesado.clear()
            nomeMaisPesado.append(nome)
        if peso < menorPeso:
            menorPeso = peso
            nomeMaisLeve.clear()
            nomeMaisLeve.append(nome)
        if peso == menorPeso:
            nomeMaisLeve.clear()
            nomeMaisLeve.append(nome)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break
print('—' * 50)
print(f'Foram cadastradas {cadastros} pessoas')
print(f'As pessoas mais pesadas foram {nomeMaisPesado} com {maiorPeso}kg')
print(f'As pessoas mais leves foram {nomeMaisLeve} com {menorPeso}kg')
print('—' * 50)

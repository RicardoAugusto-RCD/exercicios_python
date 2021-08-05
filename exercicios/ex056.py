
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maisVelho = 0
menores20 = 0
nomeMaisVelho = ' '

for c in range(1, 5):
    print('»»»»» {}ª PESSOA «««««'.format(c))
    nome = str(input('Nome: '.format(c))).upper()

    idade = int(input('Idade: '.format(c)))
    somaIdade += idade

    sexo = str(input('Sexo: [M/F]: '.format(c))).strip().upper()[0]

    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

    if sexo == 'F':
        if idade < 20:
            menores20 += + 1

mediaIdade = somaIdade / 4
print('↔' * 70)
print('A média de idade do grupo é: {} anos'.format(mediaIdade))
print('O nome do homem mais velho é {}, e ele tem {} anos'.format(nomeMaisVelho, maisVelho))
print('Existem {} mulheres com menos de 20 anos'.format(menores20))
print('↔' * 70)
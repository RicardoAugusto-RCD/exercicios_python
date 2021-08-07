
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se
# o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

separador = ('─' * 40)
total18 = totalHomens = totalMulheres20 = 0

while True:
    print(separador)
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheres20 += 1
    print(separador)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N} ')).strip().upper()[0]
    if resposta == 'N':
        break

print(separador)
print(f'Total de pessoas com mais de 18 anos foi {total18}')
print(f'Ao todo temos {totalHomens} homens cadastrados')
print(f'E temos {totalMulheres20} mulheres com menos de 20 anos')
print(separador)
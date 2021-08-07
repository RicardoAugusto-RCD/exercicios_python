
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se
# o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

separador = ('─' * 40)

sexo = ("M", "m", "F", "f")
resposta = ("S", "s", "N", "n")
contadorIdade = contadorHomens = contadorMulheres = 0

while True:
    print(separador)
    print(F'{"CADASTRO DE PESSOAS":^40}')
    print(separador)
    idade = int(input('Qual a idade? '))

    if idade >= 18:
        contadorIdade += 1

    escolhaSexo = str(input('Qual o sexo? [M/F] ')).upper().strip()[0]
    while escolhaSexo not in sexo:
        escolhaSexo = str(input('Qual o sexo? [M/F] ')).upper().strip()[0]

    if escolhaSexo in 'Mm':
        contadorHomens += 1

    if escolhaSexo in 'Ff' and idade < 20:
        contadorMulheres += 1

    print(separador)
    escolhaResposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while escolhaResposta not in resposta:
        escolhaResposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if escolhaResposta in 'Nn':
        print(separador)
        print('Programa Encerrado')
        break
print(separador)
print(f'Existem {contadorIdade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {contadorHomens} homens.')
print(f'Existe {contadorMulheres} mulheres com menos de 20 anos.')
print(separador)

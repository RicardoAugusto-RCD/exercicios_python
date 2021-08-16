
# Crie um programa que leia nome. sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final mostre:
# a) Quantas pessoas foram cadastradas.
# b) A média de idade do grupo.
# c) Uma lista com todos as mulheres.
# d) Uma lista com todas as pessoas com idade acima da média.

pessoa = dict()
pessoasLista = list()
somaIdade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']

    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print(' ► ERRO ◄ |Responda apenas M ou F|')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]

    pessoasLista.append(pessoa.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print(' ► ERRO ◄ |Responda apenas S ou N|')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('—' * 50)
print(f'a) Ao todo temos → {len(pessoasLista)} pessoas cadastradas')

media = somaIdade / len(pessoasLista)
print(f'b) A média de idade é de → {media:.2f} anos')

print(f'c) As mulheres cadastradas foram → ', end='')
for contador in range(0, len(pessoasLista)):
    if pessoasLista[contador]['sexo'] == 'F':
        print(f'{pessoasLista[contador]["nome"]} ', end='')
print()

print(f'd) Lista da pessoas que estão acima da média:')
for contador in range(0, len(pessoasLista)):
    if pessoasLista[contador]['idade'] >= media:
        print(f' → nome = {pessoasLista[contador]["nome"]} → sexo = {pessoasLista[contador]["sexo"]} '
              f' → idade = {pessoasLista[contador]["idade"]} ')
print('—' * 50)


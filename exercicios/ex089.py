
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# um boletim contendo a média de cada um, e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
contador = 0

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    contador += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break
print(f'{" BOLETIM ":—^30}')
print(f'{"No."} | {"NOME":<12} | {"MÉDIA"}')
print('—' * 30)
for i, l in enumerate(ficha):
    print(f'{i:<3} | {l[0]:<12} | {l[2]:>5.1f}')

while True:
    print('—' * 50)
    notas = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))

    if notas == 999:
        break
    else:
        if notas < contador:
            print(f'As notas de {ficha[notas][0]} são {ficha[notas][1][0]} e {ficha[notas][1][1]}')
        else:
            print(f'Posição inválida')
            continue

print('→' * 15, 'FIM DO PROGRAMA', '←' * 15)

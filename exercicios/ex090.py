
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

aluno = dict()


aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('—' * 30)
for keys, valor in aluno.items():
    print(f'→ {keys} é igual a {valor} ←')
print('—' * 30)
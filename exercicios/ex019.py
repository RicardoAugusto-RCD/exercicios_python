
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido.

import random
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)

print('{} foi escolhida(o) para apagar o quadro.'.format(sorteio))



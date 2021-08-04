
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# Média abaixo de 5.0: REPROVADO.
# Média entre 5.0 e 6.9 : RECUPERAÇÃO.
# Média 7.0 ou superior: APROVADO.

nota1 = float(input('Digite a 1ª nota: '))

nota2 = float(input('Digite a 2ª nota: '))

mediaNota = (nota1 + nota2) / 2
print('A média da 1ª nota {:.1f} e 2ª nota {:.1f} foi: {:.1f}.'.format(nota1, nota2, mediaNota))

if mediaNota < 5:
    print('Aluno Reprovado!')

elif mediaNota >= 5 and mediaNota <= 7:
    print('Aluno em Recuperação!')

else:
    print('Aluno Aprovado!')

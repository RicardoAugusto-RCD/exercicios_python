
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$'))

novoSalario = salario * 1.15

print('Com o aumento de 15%, o salário de R${:.2f} passará a valer R${:.2f}'.format(salario, novoSalario))
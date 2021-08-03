
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Informe o salário: R$ '))

if salario > 1250:
    novoSalario = salario * 1.10
    print('O salário de R$ {:.2f}, passará a valer R$ {:.2f}'.format(salario, novoSalario))
else:
    novoSalario = salario * 1.15
    print('O salário de R$ {:.2f}, passará a valer R$ {:.2f}'.format(salario, novoSalario))

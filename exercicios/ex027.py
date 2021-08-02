
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente:
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite seu nome completo: ')).strip()

primeiro = nome.split()
print('Seu primeiro nome é {}'.format(primeiro[0]))

ultimo = nome.split()
print('Seu último nome é {}'.format(ultimo[-1]))

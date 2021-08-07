
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

separador = ('─' * 50)
cedula50 =cedula20 = cedula10 = cedula1 = 0

print(f'{" BANK OF SEUCUCA QUÉEU ":—^50}')

valorSaque = int(input('Que valor você quer sacar? R$ '))

if valorSaque >= 50:
    cedula50 = valorSaque // 50
    valorSaque = valorSaque % 50

if valorSaque >= 20:
    cedula20 = valorSaque // 20
    valorSaque = valorSaque % 20

if valorSaque >= 10:
    cedula10 = valorSaque // 10
    valorSaque = valorSaque % 10

if valorSaque >= 1:
    cedula1 = valorSaque // 1
    valorSaque = valorSaque % 1

print(separador)
print(F'Total de {cedula50} cédulas de R$50')
print(F'Total de {cedula20} cédulas de R$20')
print(F'Total de {cedula10} cédulas de R$10')
print(F'Total de {cedula1} cédulas de R$1')
print(separador)
print(f'{" VOLTE SEMPRE AO BANK OF SEUCUCA QUÉEU ":—^50}')
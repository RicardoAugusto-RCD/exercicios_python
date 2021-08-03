
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

reta1 = float(input('Digite o valor da reta 1: '))

reta2 = float(input('Digite o valor da reta 2: '))

reta3 = float(input('Digite o valor da reta 3: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Forma um triângulo? Sim')
else:
    print('Forma um triângulo? Não')
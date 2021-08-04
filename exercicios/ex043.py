
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso.
# Entre 18.5 e 25: Peso Ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade Mórbida.

peso = float(input('Digite seu peso: (kg) '))

altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura ** 2)
print('O índice de IMC é: {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')

elif imc > 18.5 and imc < 25:
    print('Peso Ideal')

elif imc > 25 and imc < 30:
    print('Sobrepeso')

elif imc > 30 and imc < 40:
    print('Obesidade')

else:
    print('Obesidade Mórbida')
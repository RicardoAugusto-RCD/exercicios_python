
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e
# comprimento) e mostre a área do terreno.

def area():
    print('—' * 30)
    print(f'{"Calculando a área":^30}')
    print('—' * 30)
    largura = float(input('LARGURA [m]: '))
    comprimento = float(input('COMPRIMENTO [m]: '))
    area_terreno = largura * comprimento
    print('—' * 30)
    print(f'A área de um terreno {largura} x {comprimento} é de {area_terreno}m²')
    print('—' * 30)


area()

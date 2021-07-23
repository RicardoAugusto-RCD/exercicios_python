
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Qual a altura da parede?'))
altura = float(input('Qual a largura da parede?'))

area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))

tinta = area / 2
print('Com a área de {}m², voçê precisará de {} litros de tinta'.format(area, tinta))
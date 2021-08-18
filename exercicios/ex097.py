
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!)
# Saída:
# —————————————
#  Olá, Mundo!
# —————————————

def escreva(texto):
    #texto = str(input('Digite: '))
    print('—' * (len(texto) + 3))
    print(f'{texto:^{len(texto) + 3}}')
    print('—' * (len(texto) + 3))

escreva('Olá, Mundo!')
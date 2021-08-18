
# Faça um programa que tenha função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
# contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

def contador(i, f, p):
    from time import sleep
    print('—' * 50)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM')



contador(1, 10, 1)
contador(10, 0, 2)
print('—' * 50)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
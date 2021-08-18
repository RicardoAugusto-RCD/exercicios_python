
# Faça um programa que tenha função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
# contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

def contador(inicio, fim, passo):
    from time import sleep
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
                sleep(0.5)
                print(f'{c}', end=' ► ')
        print('FIM')

    else:
        for c in range(inicio, fim - 1, -passo):
            sleep(0.5)
            print(f'{c}', end=' ► ')
        print('FIM')

print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('—' * 50)

print('Contagem de 10 a 0 de 2 em 2')
contador(10, 0, 2)
print('—' * 50)

print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: '))
         )
print('—' * 50)

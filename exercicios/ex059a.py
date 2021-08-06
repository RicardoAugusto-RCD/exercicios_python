
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('►◄' * 20)
n1 = int(input('Primeiro valor: '))
print('►◄' * 20)
n2 = int(input('Segundo Valor: '))
print('►◄' * 20)
opcao = 0

while opcao != 5:
    print('►◄' * 20)
    print('''    ► 1 ◄ Somar
    ► 2 ◄ Multiplicar
    ► 3 ◄ Maior
    ► 4 ◄ Novos Números
    ► 5 ◄ Sair do Programa''')
    print('►◄' * 20)
    opcao = int(input('Digite sua opção ►►►►► '))
    print('►◄' * 20)

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação de {} x {} é {}'.format(n1, n2, multiplica))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        else:
           print('Os valores {} e {} são iguais'.format(n1, n2))

    elif opcao == 4:
        print('►◄' * 20)
        n1 = int(input('Primeiro valor: '))
        print('►◄' * 20)
        n2 = int(input('Segundo Valor: '))
        print('►◄' * 20)

    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção Inválida...Tente Novamente...')
    print('►◄' * 20)

print('Fim do programa! Volte Sempre!')
print('►◄' * 20)



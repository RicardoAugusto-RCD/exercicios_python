
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: '))

if expressao.count('(') % 2 == 0 and expressao.count(')') % 2 == 0:
    print('Expressão válida')

else:
    print('Expressão inválida')
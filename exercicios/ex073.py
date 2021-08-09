
# Crie uma tupla com os 20 primeiros colocados no Campeonato Brasileiro de Futebol, na ordem de colocação. Depois
# mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

brasileirao = ('Palmeiras', 'AtléticoMg', 'Fortaleza', 'Bragantino', 'AthleticoPr', 'Flamengo', 'Ceará', 'Bahia',
               'Flluminense', 'Santos', 'AtléticoGo', 'Corinthians', 'Internacional', 'Juventude', 'São Paulo',
               'América', 'Cuiabá', 'Sport', 'Grêmio', 'Chapecoense')

for contador in range(0, 5):
    print(f'{contador + 1}º {brasileirao[contador]}')

print('—' * 30)
for contador in range(16, 20):
    print(f'{contador + 1}º {brasileirao[contador]}')

print('—' * 30)
print(sorted(brasileirao))

print('—' * 30)
encontrar = brasileirao.index('Chapecoense') + 1
print(f'A Chapecoense se encontra na {encontrar}ª posição do BR21')

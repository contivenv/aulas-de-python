# bebidas = ''
# input(f'Digite suas cinco bebidas favoritas: ')
# bebidas = []
# print(f'Aqui está a lista da suas bebidas favoritas: {bebidas}')

bebidas = []
"""
Nome da lista vai ser bebida e a lista vai estar vazia, porque não sabemos
os valores que o usuário vai nos indicar.
"""
for i in range(5): # criar um laço 'for' que execute cinco vezes essa chamada
    print(f'Digite suas bebidas favoritas: ') # digitar os nomes das bebidas favoritas
    bebida = input()
    bebidas.append(bebida)

bebidas.sort() # a função 'sort' ele classifica e ordena o conteúdo da lista automaticamente

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde !')
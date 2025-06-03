import random


# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1, 50)
#     print(f'Número gerado: {n}')

# valor = random.random()
# print(f'Número ferado: {round(valor * 10, 2)}')

# valor = random.uniform(1, 100)
# print(f'Número: {round(valor, 4)}')

lista = [1, 2, 4, 6, 90, 49, 21, 40, 50, 34, 66, 210]
# n = random.choice(lista)
# print(f'Número escolhido: {n}')

# n = random.sample(lista, 3)
# print(f'Números escolhidos: {n}')

# embaralhar aleatório
print(f'Exibir a lista original: {lista}')
print(f'Bagunçar lista e exibir ela: ')
n = random.shuffle(lista)
print(lista)
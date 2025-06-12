# Podem armazenar dados em chave e valor. São similires a arrys de outras linguagens.

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
# para realizar uma busca de informação dentro do nosso dicionário, seguimos o formato abaixo. Elemento é uma string | valor drento da chave é variável | 'nome' é o valor que eu quero dentro d dicionário.
print(f'Elemento:  {elemento['nome']}')
print(f'Densidade:  {elemento['densidade']}')
print(f'O dicionário possui {len(elemento)} elementos.') # lista quantos elementos existem dentro do dicionário

# atualizar uma entrada do dicionário
elemento['grupo'] = 'Alcalinos' # Metais Alcalinos para somente Alcalinos
print(elemento)

# Adicionar uma entrada
elemento['período'] = 1
print(elemento)


# # exclusão de itens em dicionários
# del elemento['período']
# print(elemento)

# # apagar todos os itens
# elemento.clear()
# print(elemento) # o disionário ainda continua existindo porque existe um espaço alocada na memória RAM da máquina com ele ainda lá, tanto que até conseguimos alocar valores a ele ainda.

# # apagar com ele de uma vez, tirar ele da memória
# del elemento
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')

# lista: representa uma sequeência de valores armazedos na memória

# sitaxe: nome_da_lista = [valores]

# notas = [1, 2, 3, 4, 5]
# print(notas)

# n1 = [1, 2, 4, 5, 6]
# n2 = [10, 30, 40, 20, 90]

# valores = n1 + n2
# valores[0] = 9 # atribui um valor diferente para o primeiro item da lista
# print(valores[0:2]) # colocar um valor negativo acessa o último item da lista
# print(len(valores))
# print(sorted(valores, reverse=True)) # inverte o estado da lista do maior para o menor
# print(sum(valores)) # função de soma
# print(min(valores)) # função de valor mínimo
# print(max(valores)) # função de valor máximo

# valores.append(13) # a função 'append' acrescenta um valor a lista
# print(valores)
# valores.pop() # retira o último elemento da lista se não especificarmos nada, mas também retira algum do meio caso colocarmos um valor
# print(valores)
# valores.insert(3, 21) # ele coloca o valor na lista e empurra os demais para frente, sem trocar nenhum valor
# print(valores)
# print(12 in valores) # retorna True ou False se o número procurado está na lista

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Neturno']
for planeta in planetas:
    print(planeta)
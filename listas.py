# lista: representa uma sequeência de valores armazedos na memória

# sitaxe: nome_da_lista = [valores]

# notas = [1, 2, 3, 4, 5]
# print(notas)

n1 = [1, 2, 4, 5, 6]
n2 = [10, 30, 40, 20, 90]

valores = n1 + n2
valores[0] = 9 # atribui um valor diferente para o primeiro item da lista
# print(valores[0:2]) # colocar um valor negativo acessa o último item da lista
print(len(valores))
print(sorted(valores, reverse=True)) # inverte o estado da lista do maior para o menor
print(sum(valores))
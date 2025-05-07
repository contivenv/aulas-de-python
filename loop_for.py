# Exemplo de for 1

nome = 'Guilherme Conti Teixeira'
lista = [1, 3, 4, 5, 9]
numero = range (1, 10)

for letra in nome:
    print(letra)

# Exemplo de for 2 - interando sobre uma lista

for numero in lista:
    print(numero)

# Exemplo de for 3 - iterando sobre um range

"""
range(valor_inicial, valor_final)
OBS: O valor finali não é inclusivo, na verdade é do 1 ao 9.
"""

for numero in range(1, 10):
    print(numero)

# Exemplo da documentação que o Python nos explica da função if

x = int(input("Insira um número inteiro: "))

if x < 0:
    x = 0
    print('Negativo alterado para zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Um')
else:
    print('Mais')

"""
Pode haver zero ou mais partes elif, e a parte else é opcional. 
A palavra-chave ‘elif’ é uma abreviação para ‘else if’, e é útil para evitar indentação excessiva. 
Uma sequência if … elif … elif … substitui as instruções switch ou case, encontrados em outras linguagens.

Se você está comparando o mesmo valor com várias constantes, ou verificando por tipos ou atributos específicos, você também pode achar a instrução match útil. Para mais detalhes veja Instruções match.
"""

# Exemplo de documentação para função for

# Mede algumas strings:
palavras = ['gato', 'janela', 'defenestrar']
for p in palavras:
    print(p, len(p))

"""
A instrução for em Python é um pouco diferente do que costuma ser em C ou Pascal.
 
Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal), ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), a instrução for do Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. 
"""
# Código que modifica uma coleção sobre a qual está iterando pode ser inseguro. No lugar disso, usualmente você deve iterar sobre uma cópia da coleção ou criar uma nova coleção:

# Cria uma amostra de coleção
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Estratégia: iterar por uma cópia
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Estratégia: criar uma nova coleção
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

nome = 'Guilherme Conti Teixeira'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em lista

for _, letra in enumerate(nome):
    print(letra)

'''Quando não precisamos de um valor, podemos usar o _ para desacartar um valor'''

for valor in enumerate(nome):
    print(valor)
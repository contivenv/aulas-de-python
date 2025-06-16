# Funções de blocos de códigos, onde dá o valor de uma função.
# Modularização criando uma bloco de códigos que faz determinada função.
# Reúso dos códigos e melhora a legibilidade do código.

# def <nome_função> ([argumento]): # criar funções em python usamos a palavra "def" em Python. Crie um objeto, atribui um nome a ele e codifica esse objeto colocando um bloco de códigos dentro dele.
#     <intruções>

# função sem argumentos, só pra teste.

# def mensagem(): # a função foi definida, foi criada, está na memória, mas ainda não foi usada. Cria ela e ela fica esperando o momento certo para ser usada.
#     print('Guilherme Conti Teixeira')
#     print('Aluno de programação')

# mensagem()

# função com argumentos

# def soma(a, b):
#     print(a+b)

# soma(12, 7) # automaticamente o valor 12 é copiado para o argumento "a" e 7 a "b", que na verdade, se tornam variáveis dentro da função. O somatório desses valores vai aparecer na tela.

def mult(x, y):
    return x * y # a função encerra quando a função 'return' é encontrada.

# a = 5
# b = 8
# c = mult(a, b)
# print(f'O produto de {a} e {b} é {c}') # resultado: O produto de 5 e 8 é 40

# def div(k, j):
#     if j != 0:
#         return k / j 
#     else:
#         return 'Impossivel dividir por zero !' # fizemos uma forma de tratamento primario de dados, classificando as divisões em zero impossíveis.

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}') # não podemos colocar a divisão por zero.

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9, 12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)


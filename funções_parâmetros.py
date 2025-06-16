# def contar(num=11, caractere='+'): # vai escrever um caracter x número de vezes
#     for i in range(1, num):
#         print(caractere)


x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c == 0:
        return a * b # se passarmos dois argumentos, ele faz a divisão e se passarmos os três, ele executa a função 'return' de baixo. Resultado aqui é 30
    else:
        return a + b + c # resultado aqui é 14

if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)
    # contar(caractere= '&') # executa uma tarefa que vai aparecer na tela. Nesse caso ele vai substituir o caracter '+' para '&'
    # contar(num=8, caractere='@') # na pratica, não precisamos ecrever os caracteres específicos ou argumentos, podemos fazer igual o exemplo abaixo:
    # contar(6, '@') # só preciso escrever os parâmetros quando eles estiverem fora de ordem.



    """
Os valores que colocamos antes na função precisam ser como aleatórios sempre primeiros e definidos depois para não der problema. Vamos dar um exemplo logo abaixo:


def contar(caractere, num=11): # vai escrever um caracter x número de vezes # se passarmos o mouse em cima de caractere, ele marcar como "any" de qualquer e em 'num' como "int" de inteiro.
    for i in range(1, num):
        print(caractere)

    """



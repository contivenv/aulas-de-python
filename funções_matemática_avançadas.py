# funções builtin (internas)
# valores = [2,45,6,8,12,-4,-5,2]
# print(max(valores)) # exibe o valor máximo da lista 'valores'
# print(min(valores)) # exibe o valor mínimo da lista 'valores'

# a = -5
# b = 4
# print(abs(a)) # valor absoluto do número, no caso, 5
# print(pow(a, b)) # função 'pow' é uma função de exponenciação, resultado de valor 625
# c = 2.789011
# print(round(c,3)) # função 'roud' faz o arredontamento do valor numérico. No caso, pedimos para ele arredondar até 3 casas decimais, tento o valor de 2.789.

import math

x = 8
y = 100

# raiz_quadrada = math.sqrt(x) # calcular a raiz quadrada de 8
# print(math.ceil(raiz_quadrada)) # exibir resultado da raiz quadrada (2.8284271247461903) | função 'ceil' arredonda para cima e 'floor' arredoandar para o inteiro para baixo.

# logaritmo = math.log10(y) # calcula o logaritmo do valor
# print(logaritmo) # resultado 2.0

print(math.pi) # valor de pi com máxima precisão da máquina (3.141592653589793)
print(math.factorial(x)) # valor factorial de 8 (40320)
print(x / math.inf) # valor de infinito (0.0)

"""
Caso em algum momento precisemos estudar mais afundo as funções disponiveis da biblioteca math que no caso,
são muitas, podemos consultar a documentação em: https://docs.python.org/pt-br/3.13/library/math.html
"""
"""
O que é um escopo ? 
Um escopo é o que vai indicar a visibilidade de uma variável dentro do código.

Existem dois tipos de escopo: o Global e o Local. 

Local -> A local ela é criada somente dentro de um escopo ou rotina, sendo inicializada todas às vezes que a função é inicializada. De fora não conseguimos acessar.
Global -> usada para valores que são constantes no programa e acessíveis pra todas às funções, mas temos que tomar cuidado com variáveis globais, optar sempre pelas locais.
"""

var_global = "Curso Completo de Python"

def escreve_texto():
    var_local = "Guilherme Conti Teixeira"
    print(f'Variável global: {var_global}')
    print(f'Variável local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável global: {var_global}')
    print(f'Variável local: {var_local}') # NameError: name 'var_local' is not defined. Did you mean: 'var_global'? Podemos acessar ela somente dentro do bloco. Só pode ser usada dentro da função.



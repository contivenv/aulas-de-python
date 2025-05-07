"""
Usar estruturas condicionais podem ser uma forma eficiênte e inteligente de otimizar
nosso programa que estamos fazendo, poque usando elas, podemos ter vários caminhos diferentes
e ter diversas soluções.
"""
idade = 18

if idade < 18:
    print('Menor de idade') # A inicialização de um novo bloco em Python sempre vai começar depois de um espaço de quadro linhas, assim como nesta linha, uma indentação.
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade') # para começar uma indentanção nova, precisa-se colocar os ":" e os quadro espaços.

"""
Em Python, if, else e elif são estruturas condicionais usadas para controlar o fluxo do programa com base em condições. Aqui está uma explicação simples:

1. if (se)

    Verifica se uma condição é verdadeira.

    Se for verdadeira, executa o bloco de código dentro dele.
"""

# Exemplo

if idade >= 18:
    print("Você é maior de idade.")

"""
2. else (senão)

    Executa um bloco de código se a condição do if for falsa.

    Não tem condição (só entra quando o if falha).
"""

# Exemplo:

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

"""
3. elif (senão se)

    Usado para testar outra condição se o if anterior for falso.

    Pode ter vários elifs antes de um else.
"""

# Exemplo

nota = 4.9

if nota >= 9:
    print("Aprovado com mérito!")
elif nota >= 6:
    print("Aprovado.")
else:
    print("Reprovado.")

"""
Resumo:

    if: Testa uma condição (se).

    elif: Testa outra condição se o if anterior for falso (senão se).

    else: Executa se todas as condições acima forem falsas (senão).

É como um "fluxo de decisões" no código
"""
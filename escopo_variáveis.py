numero = 42
print(numero)
print(type(numero))

"""

Variáveis globais são reconhecidas no escopo de TODO O PROGRAMA

Variáveis locais sõa reconhecidas apenas onde foram declaradas, seu escopo é limitado
ao bloco onde ela foi declarada.
"""

if numero > 10:
    novo = numero + 10
    print(novo) # não é reconhecida fora do bloco, uma variável local.

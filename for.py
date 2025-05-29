# estrutura do laço for
# for --variával-- in --sequência:--
    # comando para execução

# lista = [1, 2, 4, 5, 6, 9, 10]

# for item in lista: # operador "in" é um operador de associação
#     print(item)

# lista = [1, 2, 4, 5, 6, 9, 10]
# palavra = 'Computador'
# for letra in palavra: # operador "in" é um operador de associação
#     print(letra)

# for numero in range(1, 10): # função "range"significa que é uma faixa que vai pegar do primeiro número até o penultimo número
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}') # o x+1 fala ao programa que o nome que quero que seja exibido seja a partir do número 1

#  range(valor_inicial, valor_final, incremento)

# for x in range(2, 20):
#     print(x)

pedra = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamente', 'Turmalina')

for pedra in pedra:
    if pedra == 'Quartzo':
        continue # encerra a iteração atual do laço. A proxima instrução do for não será executada, mas o laço não termina, quem termina o laço é a instrução break.
    print(pedra)

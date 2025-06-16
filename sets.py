# sets = conjutos em português. Set = armazenam itens não duplicados, não conseguimos modificar os itens dentro deles, mas eles são mutaveis.

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
# print(len(planeta_anao))
# print('Ceres' in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros, end='')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte',}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa'}
# print(astros1 | astros2) # para juntar as duas listas, podemos apenas colocar '|'  e lembrando que elas não vão aparecer duplicadas.

astros1.add('Urano')
astros1.add('Sol') # adciona um elemento
# astros1.discard('Lua') # remove um elemento
# astros1.pop() # remove um elemento de forma aleatória; podemos aproveitar esses elementos em jogos, por exemplo.
astros1.clear() # limpa o conjuto todo

# a ordem dos conjuntos vem em uma ordem qualquer quando acessamos eles.
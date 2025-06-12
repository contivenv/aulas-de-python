# Set = armazenam itens não duplicados, não conseguimos modificar os itens dentro deles, mas eles são mutaveis.

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))
# print('Ceres' in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros, end='')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte',}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa'}
print(astros1 | astros2) # para juntar as duas listas, podemos apenas colocar '|'  e lembrando que elas não vão aparecer duplicadas.
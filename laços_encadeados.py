# for contador_externo in range (1,6):
#     print(f'\nRodada: {contador_externo}')
#     for contador_interno in range(5,0, -1):
#         print(f'Valor: {contador_interno}')
# print('Fim do laço')

import random # biblioteca de randomização

for A in range(1,6):
    print(f'\Conjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')

# são imutáveis os contaúdos das tuplas

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (1,2,3,4,5,6,7,8,9,0)
# print(t1.cout(5)) # funçao 'cout' exibe quantas vezes aparece o número 5 na lista.
# print(halogenios[:3]) # fazer slice para a lista
# print('Cl' in halogenios) # operador 'in' para verificar se o item está presente nas tuplas
# print(sum(t1))

# operadores não disponíveis nas tuplas: .sort(), .append(), reverse(), .pop()... ou seja, tudo que altere o valor da tupla.

# for elemento in elementos:
#     print(f'Elementos quimicos: {elemento}')

# grupo17 = list (halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr' ]
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))

# tuplas são bem parecidas com lista, a diferença delas são seu fator de umutabilidade das tuplas.

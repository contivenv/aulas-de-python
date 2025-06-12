# são imutavei, consegue mudar a variável que contem a string

# nome = 'Aluno'
# aluno = 'Guilherme'
# # letra = nome[2]
# # print(letra)
# # print(len(nome))
# print(nome + ' é o ' + aluno)

# frase = 'Iremos aprender Python hoje'
# palavras = frase.split()
# print(palavras[1])
# for letra in frase:
#     print(letra)

# print(frase[0:5])

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste.upper()) # função 'uppee' para deixar todas as letras em maiúsculo; função 'capitalize' deixa tudo em minúsculo; função 'title' deixa cada letra de cada frase em maiúscula.

# suplemento = 'cloreto de magnésio'
# novo_suplemento = suplemento.replace('magnésio', 'zinco') # função 'replace' para substituir alguma palavra na string. Sempre temos que colocar  ('nome_que_vai_trocar', 'nome_que_vai_no_lugar')
# print(suplemento)
# print(novo_suplemento)

# frase = '        Programação é bom  !   '
# print(frase)
# print (frase.lstrip()) # L de left (esquerda)
# print (frase.rstrip()) # R de right (direita)
# print (frase.strip()) # Esquerda e direita ao mesmo tempo

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20)) # dê 20 espaços no total de justifique a palavra a direita
# print(fruta.center(20)) # alinha no centro com os 20 espaços
# print(fruta.ljust(20, "-")) # na esquerda com os traços
# print(fruta.center(20, "-")) # centralizado com os traços

# p = 'Curso de python'
# print(p.startswith('Cu')) # pergunta se essas letras começam a frase
# print(p.endswith('on')) # pergunta se essas letras terminam a frase

# Docsstrigs

texto = """
Docstring  é uma espécie de documentação que podemos
inserir dentro de um módulo, função ou clase no Python
entre outros locais.
    Respeita deslocamento do texto e é multilinhas
"""
print(texto)

# https://docs.python.org/3/library/stdtypes.html#string-methods documentação sobre strings
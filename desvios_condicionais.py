# Simples, composto ou encadeado - essas são as principais

# Exemplo simples de condicioanal - notas da faculdade com SPA
a1 = a2 = a3 = 0.0
media = 0.0

a1 = float(input('Digite a primeira nota: '))
a2 = float(input('Digite a segunda nota: '))
a3 = float(input('Digite a segunda nota: '))

# Calcular a média aritimética das notas
media = (a1 + (a2 * 2) + a3) / 4

if (media >= 4.9): # se a média for maior ou igual a 5
    print('Resultado: Aprovado') # indentação realiazada. Tudo que estiver edentro dela, vai ser executado pela linha de código acima
if (media <= 4.9):
    print('Resultado: Reprovado')

print('Sua média é {}'.format(media)) # formatando o conteúdo da variável para que ela apareça dentro da chave

# Exemplo simples de condicioanal - notas da faculdade sem SPA
a1 = a2 = 0.0
media = 0.0

a1 = float(input('Digite a primeira nota: '))
a2 = float(input('Digite a segunda nota: '))

# Calcular a média aritimética das notas
media = (a1 + (a2 * 2)) / 3

if (media >= 4.9): # se a média for maior ou igual a 5
    print('Resultado: Aprovado') # indentação realiazada. Tudo que estiver edentro dela, vai ser executado pela linha de código acima
if (media <= 4.9):
    print('Resultado: Reprovado')

print('Sua média é {}'.format(media)) # formatando o conteúdo da variável para que ela apareça dentro da chave
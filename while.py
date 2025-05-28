# exemplo simples de repetição usando o while. Nesse teste, queromos que os números sejam exibidos de 1 a 10.Exception

# num = 1

# while (num <= 1000): # while significa 'enquanto' em português
#     print(num)
#     num += 1 # esse comando significa que ele vai acescentar 1 no valor da variável, ou seja, todas as vezes que tiver uma repetição, o valor vai aumentar.
# print('Laço encerrado !')

# agora, faremos um programa onde se cada usuário inserir um dado, uma mensagem aparecera na tela, porém, se alguém apertar a tecla 'X', o programa encerra sua tarefa.

nome = None # None que dizer 'vazio'. Usamos ela porque não sabemos quem vai digitar os dados, é uma variável vazia.

while True:
    print('Digite seu nome ou digite X para parar: ')
    nome = input()
    if nome == 'X' or nome == 'x': # diferenciação de minúsculo para maiúsculo / ou um, ou outro vai retornar True. Quando retornar, vai executar a função 'break'. A instrução break ela finaliza imediatamente o laço de repetição onde ela está inserida no bloco.
        break
    print(f'Bem vindo {nome}') # f-string sendo usado
print('Até mais !')

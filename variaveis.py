nome_usuario = 'Guilherme Conti Teixeira' # strig de caractéres
print(nome_usuario) # coloca os argumentos para exibir esses dados
# os nomes são CaseSensitive, ele diferencia minúsculas de maiúsculas

media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Guilherme', 21 # como as variáveis não vão receber o mesmo valor, as que são passadas depois da vírgula o Python já atribui o valor
# em Python, não precisamos declarar o tipo de dado que estamos colocando. Ele sabe o que éum float, uma string, um número inteiro conforme a cadeia de caractéres que colocamos
status = True # valor lógico, tipo booleano


# tipos de dados
print(type(media)) # int
print(type(n2)) # float
print(type(nome)) #str
print(type(status)) # bool
print(type(1+2j)) # complex

# Função isinstance()
a = 10
b = 'Sol'
print(isinstance(1, (int, str))) # essa função vai verificar se esse dado que você está colocando corresponde ao tipo de dado anexado logo a frente. Se sim, ele retorna True e senão, False

a = 40
c = 3
r = a * c
print(r)
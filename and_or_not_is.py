<<<<<<< HEAD
"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is

Operadores binários:
    - and, or
"""

# Regras de funcionamento
# para o operador binário 'and' ambos precisam ser vardadeiros
# para 'or', um ou outro valor precisa ser verdadeiro

ativo = True
logado = True
nome = input('Insira seu nome: ')
if ativo and logado:
    print('Bem-vindo', nome, '!')
else:
    print('Você precisa ativar a sua conta. Verifique seu e-mail')
if not ativo:
    print('VOcê precisa ativar a sua conta. Pra favor, verifique seu e-mail')
else:
    print('Bem-vindo', nome, '!')

"""
 Em Python, and, or, not e is são operadores lógicos e de comparação usados para testar condições. Aqui está uma explicação simples e direta:

 1. and (E lógico)

    Retorna True se todas as condições forem verdadeiras.
 """

# Exemplo

idade = 17
carteirinha = False

if idade >= 18 and carteirinha:
    print("Pode entrar no evento.")
else:
    idade < 18 and carteirinha
    print("Some daqui !")


"""
2. or (OU lógico)

    Retorna True se pelo menos uma das condições for verdadeira.
"""

# Exemplo

if tem_passagem or eh_convidado:
    print("Pode entrar no show.")

"""
3. not (NEGAÇÃO)

    Inverte o valor booleano:

        Se algo é True, vira False (e vice-versa).

(Só entra se bloqueado for False).
"""

# Exemplo

if not bloqueado:
    print("Acesso permitido.")

"""
4. is (COMPARAÇÃO DE IDENTIDADE)

    Verifica se dois objetos são o mesmo (não só iguais, mas a mesma instância na memória).

    Usado principalmente com None, True e False.
"""

# Exemplo

if resultado is None:
    print("Nenhum resultado encontrado.")

"""
Resumo rápido:
Operador	Função	Exemplo

and	--- E lógico (todos True) --- if x > 0 and y < 10:

or --- OU lógico (pelo menos um True) --- if vip or idade >= 65:

not --- Inverte o valor --- if not erro:

is --- Mesmo objeto? --- if valor is None:

Dica importante:

    == compara valores (ex: 10 == 10 → True).

    is compara a identidade (ex: lista1 is lista2 só é True se for o mesmo objeto).
"""

# Exemplo: Sistema de acesso com verificações lógicas

# Dados do usuário (simulados)
usuario_registrado = "admin"
senha_registrada = "1234"
nivel_acesso = "admin"
bloqueado = False
token = None

# Tentativa de login
usuario_input = input("Digite seu usuário: ")
senha_input = input("Digite sua senha: ")

# Verificações combinadas (usando and, or, not e is)
if (usuario_input == usuario_registrado and senha_input == senha_registrada):
    if not bloqueado:
        print("Login bem-sucedido!")
        
        # Verifica se é admin OU tem token válido
        if nivel_acesso == "admin" or token is not None:
            print("Acesso total liberado!")
        else:
            print("Acesso limitado.")
    else:
        print("Conta bloqueada. Contate o suporte.")
else:
    print("Usuário ou senha incorretos.")

# Verificação extra com 'is' (comparando identidade)
config_padrao = None
config_usuario = config_padrao

if config_usuario is None:
    print("\nConfiguração não definida. Usando padrão.")

"""
Explicação do código:

    and (linha 11):

        Verifica se ambos (usuario_input e senha_input) estão corretos.

    or (linha 16):

        Libera acesso total se o usuário for admin OU tiver um token válido.

    not (linha 12):

        Inverte o valor de bloqueado (se for False, vira True e permite o login).

    is (linhas 16 e 24):

        Compara se token não é None (linha 16).

        Verifica se config_usuario é exatamente None (linha 24).
"""

# Saídas possíveis: 

"""
Digite seu usuário: admin
Digite sua senha: 1234
Login bem-sucedido!
Acesso total liberado!
Configuração não definida. Usando padrão.
"""

"""
Por que usar is em vez de ==?

    is compara a identidade do objeto (ex: None, True, False).

    == compara valores.
"""

lista1 = [1, 2]
lista2 = [1, 2]
print(lista1 == lista2)  # True (valores iguais)
=======
"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is

Operadores binários:
    - and, or
"""

# Regras de funcionamento
# para o operador binário 'and' ambos precisam ser vardadeiros
# para 'or', um ou outro valor precisa ser verdadeiro

ativo = True
logado = True
nome = input('Insira seu nome: ')
if ativo and logado:
    print('Bem-vindo', nome, '!')
else:
    print('Você precisa ativar a sua conta. Verifique seu e-mail')
if not ativo:
    print('VOcê precisa ativar a sua conta. Pra favor, verifique seu e-mail')
else:
    print('Bem-vindo', nome, '!')

"""
 Em Python, and, or, not e is são operadores lógicos e de comparação usados para testar condições. Aqui está uma explicação simples e direta:

 1. and (E lógico)

    Retorna True se todas as condições forem verdadeiras.
 """

# Exemplo

idade = 17
carteirinha = False

if idade >= 18 and carteirinha:
    print("Pode entrar no evento.")
else:
    idade < 18 and carteirinha
    print("Some daqui !")


"""
2. or (OU lógico)

    Retorna True se pelo menos uma das condições for verdadeira.
"""

# Exemplo

if tem_passagem or eh_convidado:
    print("Pode entrar no show.")

"""
3. not (NEGAÇÃO)

    Inverte o valor booleano:

        Se algo é True, vira False (e vice-versa).

(Só entra se bloqueado for False).
"""

# Exemplo

if not bloqueado:
    print("Acesso permitido.")

"""
4. is (COMPARAÇÃO DE IDENTIDADE)

    Verifica se dois objetos são o mesmo (não só iguais, mas a mesma instância na memória).

    Usado principalmente com None, True e False.
"""

# Exemplo

if resultado is None:
    print("Nenhum resultado encontrado.")

"""
Resumo rápido:
Operador	Função	Exemplo

and	--- E lógico (todos True) --- if x > 0 and y < 10:

or --- OU lógico (pelo menos um True) --- if vip or idade >= 65:

not --- Inverte o valor --- if not erro:

is --- Mesmo objeto? --- if valor is None:

Dica importante:

    == compara valores (ex: 10 == 10 → True).

    is compara a identidade (ex: lista1 is lista2 só é True se for o mesmo objeto).
"""

# Exemplo: Sistema de acesso com verificações lógicas

# Dados do usuário (simulados)
usuario_registrado = "admin"
senha_registrada = "1234"
nivel_acesso = "admin"
bloqueado = False
token = None

# Tentativa de login
usuario_input = input("Digite seu usuário: ")
senha_input = input("Digite sua senha: ")

# Verificações combinadas (usando and, or, not e is)
if (usuario_input == usuario_registrado and senha_input == senha_registrada):
    if not bloqueado:
        print("Login bem-sucedido!")
        
        # Verifica se é admin OU tem token válido
        if nivel_acesso == "admin" or token is not None:
            print("Acesso total liberado!")
        else:
            print("Acesso limitado.")
    else:
        print("Conta bloqueada. Contate o suporte.")
else:
    print("Usuário ou senha incorretos.")

# Verificação extra com 'is' (comparando identidade)
config_padrao = None
config_usuario = config_padrao

if config_usuario is None:
    print("\nConfiguração não definida. Usando padrão.")

"""
Explicação do código:

    and (linha 11):

        Verifica se ambos (usuario_input e senha_input) estão corretos.

    or (linha 16):

        Libera acesso total se o usuário for admin OU tiver um token válido.

    not (linha 12):

        Inverte o valor de bloqueado (se for False, vira True e permite o login).

    is (linhas 16 e 24):

        Compara se token não é None (linha 16).

        Verifica se config_usuario é exatamente None (linha 24).
"""

# Saídas possíveis: 

"""
Digite seu usuário: admin
Digite sua senha: 1234
Login bem-sucedido!
Acesso total liberado!
Configuração não definida. Usando padrão.
"""

"""
Por que usar is em vez de ==?

    is compara a identidade do objeto (ex: None, True, False).

    == compara valores.
"""

lista1 = [1, 2]
lista2 = [1, 2]
print(lista1 == lista2)  # True (valores iguais)
>>>>>>> a9dd207ff78b65dd8288231ed0cb17996361b182
print(lista1 is lista2)  # False (objetos diferentes)
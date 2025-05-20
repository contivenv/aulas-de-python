# os principais operadores lógicos são: AND (e), OR (ou) e NOT (não)

# TABELAS VERDADE BOOLEANAS

# Operador AND (E)
# A | B | A and B
# 0 | 0 |    0
# 0 | 1 |    0
# 1 | 0 |    0
# 1 | 1 |    1

# Operador OR (OU)
# A | B | A or B
# 0 | 0 |   0
# 0 | 1 |   1
# 1 | 0 |   1
# 1 | 1 |   1

# Operador NOT (NÃO)
# A | not A
# 0 |   1
# 1 |   0

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento ? ' + str(resultado)

print(msg)

# programa de disparo de alarme
porta = 'fechada'
janela = 'fechada'

alarme = (porta == 'aberta') or (janela == 'aberta')
msg = 'Alarme disparado ? ' + str(alarme)
print(msg)

dinheiro = False
dinheiro = not dinheiro # operador lógico ele inverte o estado. Antes eu não tinha dinheiro para fazer a compra, agora eu tenho porque ele negou o estado com "not"
msg = 'Tem dinheiro para compra ? ' + str(dinheiro)
print(msg)
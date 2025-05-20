x = y = z = False
n1 = n2 = 0

print('Digite um número:')
n1 = int(input()) # dois jeitos de fazer, mas que teram o mesmo resultado no final. Pórem, uma linha de comando fica mais limpo
n2 = int(input('Digite outro número:'))

x = n1 == n2
print('São iguais ?', x, '\n') # contatenar é juntar strings para formar uma mensagem maior. O "\n" é um caracter de escape, como se fosse um enter no teclado.

z = n1 > n2
print(n1, 'é maior que', n2, '?', z, '\n')

y = n1 != n2
print('São diferentes ? ' + str(y)) # o sinal de + pode também ser usado como concatenação. Convertemos a variável do tipo booleano para string.
      
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: divisão por zero.")
except ValueError:
    print("Erro: valor inválido. Digite números válidos.")

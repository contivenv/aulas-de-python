numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Ordem crescente:", sorted(numeros))
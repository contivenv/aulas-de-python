notas = []
with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(",")
        notas.append((nome, float(nota)))

media = sum(nota for _, nota in notas) / len(notas)
print(f"Média da turma: {media:.2f}")

with open("aprovados.txt", "w") as saida:
    for nome, nota in notas:
        if nota >= 7:
            saida.write(f"{nome},{nota}\n")

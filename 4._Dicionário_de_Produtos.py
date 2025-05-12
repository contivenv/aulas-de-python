produtos = {}

# Adicionar
produtos["Arroz"] = 5.99
produtos["Feijão"] = 6.49

# Remover
produtos.pop("Feijão", None)

# Buscar
print(produtos.get("Arroz", "Produto não encontrado."))

# Listar ordenado
for nome in sorted(produtos):
    print(f"{nome}: R${produtos[nome]:.2f}")

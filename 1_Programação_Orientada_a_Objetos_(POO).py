class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_dados(self):
        print(f"{self.titulo} - {self.autor} ({self.ano})")

    def eh_antigo(self):
        return 2025 - self.ano > 50


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            livro.exibir_dados()

    def buscar_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor == autor:
                livro.exibir_dados()

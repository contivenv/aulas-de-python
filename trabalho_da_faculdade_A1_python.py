# Importa os módulos necessários
import json  # Para trabalhar com arquivos JSON
from datetime import datetime  # Para validação e manipulação de datas

# Classe que representa uma tarefa individual
class Tarefa:
    def __init__(self, descricao, data):
        """Inicializa uma nova tarefa com descrição e data"""
        self.descricao = descricao  # Texto descritivo da tarefa
        self.concluida = False  # Status inicial da tarefa (não concluída)
        self.data = self.validar_data(data)  # Valida e armazena a data

    def validar_data(self, data_str):
        """Valida e formata a data da tarefa"""
        try:
            # Tenta converter a string para objeto datetime
            # Usa o formato dia/mês/ano (ex: 31/12/2023)
            data_obj = datetime.strptime(data_str, '%d/%m/%Y')
            return data_str  # Retorna no formato original se válido
        except ValueError:
            # Se a conversão falhar, lança uma exceção com mensagem de erro
            raise ValueError("Data inválida. Use o formato DD/MM/AAAA")

    def concluir(self):
        """Marca a tarefa como concluída"""
        self.concluida = True

    def to_dict(self):
        """Converte o objeto Tarefa para um dicionário (útil para JSON)"""
        return {
            'descricao': self.descricao,
            'concluida': self.concluida,
            'data': self.data
        }

    @staticmethod
    def from_dict(dado):
        """Cria um objeto Tarefa a partir de um dicionário (método estático)"""
        tarefa = Tarefa(dado['descricao'], dado['data'])
        tarefa.concluida = dado['concluida']
        return tarefa

    def __str__(self):
        """Retorna uma representação em string da tarefa (para exibição)"""
        status = '✓' if self.concluida else '✗'  # Símbolos para status
        return f"[{status}] {self.descricao} (Data: {self.data})"


# Classe principal que gerencia a lista de tarefas
class GerenciadorDeTarefas:
    def __init__(self, arquivo='tarefas.json'):
        """Inicializa o gerenciador com um arquivo de armazenamento"""
        self.arquivo = arquivo  # Nome do arquivo para salvar as tarefas
        self.tarefas = []  # Lista vazia de tarefas
        self.carregar()  # Carrega tarefas existentes do arquivo

    def adicionar_tarefa(self, descricao, data):
        """Adiciona uma nova tarefa à lista"""
        try:
            nova_tarefa = Tarefa(descricao, data)
            self.tarefas.append(nova_tarefa)
            self.salvar()  # Salva as alterações no arquivo
            print("\nTarefa adicionada com sucesso!")
        except ValueError as e:
            print(f"\nErro: {e}")  # Captura erros de validação de data

    def listar_tarefas(self):
        """Exibe todas as tarefas cadastradas"""
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
            return
        
        print("\n=== LISTA DE TAREFAS ===")
        # Enumera as tarefas começando do 1 (em vez de 0)
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. {tarefa}")  # Usa o __str__ da Tarefa

    def buscar_tarefas(self, termo):
        """Busca tarefas que contenham o termo na descrição"""
        # List comprehension para filtrar tarefas
        encontradas = [
            (i, tarefa) for i, tarefa in enumerate(self.tarefas, start=1) 
            if termo.lower() in tarefa.descricao.lower()  # Busca case-insensitive
        ]
        
        if not encontradas:
            print("\nNenhuma tarefa encontrada com esse termo.")
            return
        
        print(f"\n=== TAREFAS ENCONTRADAS ({len(encontradas)}) ===")
        for i, tarefa in encontradas:
            print(f"{i}. {tarefa}")

    def concluir_tarefa(self, indice):
        """Marca uma tarefa como concluída pelo seu índice"""
        try:
            indice = int(indice)  # Converte para inteiro
            if 1 <= indice <= len(self.tarefas):
                self.tarefas[indice - 1].concluir()  # Ajusta índice para 0-based
                self.salvar()
                print("\nTarefa marcada como concluída!")
            else:
                print("\nErro: Índice inválido.")
        except ValueError:
            print("\nErro: Digite um número válido.")

    def remover_tarefa(self, indice):
        """Remove uma tarefa da lista pelo seu índice"""
        try:
            indice = int(indice)
            if 1 <= indice <= len(self.tarefas):
                tarefa_removida = self.tarefas.pop(indice - 1)  # Remove e retorna
                self.salvar()
                print(f"\nTarefa removida: {tarefa_removida.descricao}")
            else:
                print("\nErro: Índice inválido.")
        except ValueError:
            print("\nErro: Digite um número válido.")

    def salvar(self):
        """Salva todas as tarefas no arquivo JSON"""
        try:
            with open(self.arquivo, 'w') as f:
                # Converte cada tarefa para dicionário e salva com formatação
                json.dump([tarefa.to_dict() for tarefa in self.tarefas], f, indent=4)
        except IOError as e:
            print(f"\nErro ao salvar as tarefas: {e}")

    def carregar(self):
        """Carrega tarefas do arquivo JSON"""
        try:
            with open(self.arquivo, 'r') as f:
                tarefas_carregadas = json.load(f)
                # Converte cada dicionário de volta para objeto Tarefa
                self.tarefas = [Tarefa.from_dict(dado) for dado in tarefas_carregadas]
        except FileNotFoundError:
            # Se o arquivo não existe, começa com lista vazia
            self.tarefas = []
        except json.JSONDecodeError:
            print("\nAviso: Arquivo de tarefas corrompido. Iniciando com lista vazia.")
            self.tarefas = []
        except Exception as e:
            print(f"\nErro inesperado ao carregar tarefas: {e}")
            self.tarefas = []


def mostrar_menu():
    """Exibe o menu de opções e retorna a escolha do usuário"""
    print("\n=== MENU PRINCIPAL ===")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Buscar tarefas por descrição")
    print("4. Marcar tarefa como concluída")
    print("5. Remover tarefa")
    print("6. Sair")
    return input("Escolha uma opção: ")


def main():
    """Função principal que inicia o programa e gerencia o fluxo"""
    gerenciador = GerenciadorDeTarefas()  # Cria o gerenciador
    
    while True:  # Loop principal do programa
        opcao = mostrar_menu()
        
        if opcao == '1':
            # Adicionar nova tarefa
            descricao = input("Descrição da tarefa: ").strip()
            data = input("Data (DD/MM/AAAA): ").strip()
            gerenciador.adicionar_tarefa(descricao, data)
        
        elif opcao == '2':
            # Listar tarefas
            gerenciador.listar_tarefas()
        
        elif opcao == '3':
            # Buscar tarefas
            termo = input("Termo de busca: ").strip()
            gerenciador.buscar_tarefas(termo)
        
        elif opcao == '4':
            # Concluir tarefa
            gerenciador.listar_tarefas()
            if gerenciador.tarefas:  # Só mostra se houver tarefas
                indice = input("Número da tarefa a concluir: ").strip()
                gerenciador.concluir_tarefa(indice)
        
        elif opcao == '5':
            # Remover tarefa
            gerenciador.listar_tarefas()
            if gerenciador.tarefas:
                indice = input("Número da tarefa a remover: ").strip()
                gerenciador.remover_tarefa(indice)
        
        elif opcao == '6':
            # Sair do programa
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
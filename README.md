import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from rich.console import Console
from rich.table import Table
from utils import *

console = Console()

# Dicionário de opções do menu mapeando números a funções
opcoes_menu = {
    1: cadastrar_pessoa,
    2: cadastrar_cliente,
    3: cadastrar_atendente,
    4: cadastrar_tecnico,
    5: consultar_pessoas,
    6: consultar_clientes,
    7: consultar_atendentes,
    8: consultar_tecnicos,
    9: sair
}

def redirect_output_to_tkinter(text_widget):
    class TkinterOutput:
        def write(self, message):
            text_widget.insert(tk.END, message)
            text_widget.see(tk.END)

        def flush(self):
            pass  # This is needed for the stream interface

    return TkinterOutput()

def open_output_window():
    root = tk.Tk()
    root.title("Console Output")
    root.geometry("800x600")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=40)
    text_area.pack(padx=10, pady=10)

    # Redirect stdout and stderr to the tkinter text widget
    sys.stdout = redirect_output_to_tkinter(text_area)
    sys.stderr = redirect_output_to_tkinter(text_area)

    return root

def run_menu():
    root = open_output_window()

    def menu():
        while True:
            # Cria uma tabela para exibição no console
            table = Table(title="Escolha uma opção")

            table.add_column("Opção", justify="right", style="cyan", no_wrap=True)
            table.add_column("Descrição", style="magenta")

            # Adiciona as opções do menu à tabela
            table.add_row("1", "Cadastrar Pessoa")
            table.add_row("2", "Cadastrar Cliente")
            table.add_row("3", "Cadastrar Atendente")
            table.add_row("4", "Cadastrar Técnico")
            table.add_row("5", "Consultar Pessoas")
            table.add_row("6", "Consultar Clientes")
            table.add_row("7", "Consultar Atendentes")
            table.add_row("8", "Consultar Técnicos")
            table.add_row("9", "Sair")

            console.print(table)  # Exibe a tabela no console

            try:
                opcao = int(input("Opção: "))  # Solicita a opção do usuário
                funcao = opcoes_menu.get(opcao)  # Obtém a função correspondente
                if funcao:
                    funcao()  # Executa a função
                else:
                    console.print("[red]Opção inválida![/red]")  # Mensagem de erro para opção inválida
            except ValueError:
                console.print("[red]Por favor, insira um número válido.[/red]")  # Mensagem de erro para entrada inválida

    # Run the menu function in a separate thread to avoid blocking the tkinter main loop
    Thread(target=menu).start()
    root.mainloop()

if __name__ == "__main__":
    run_menu()

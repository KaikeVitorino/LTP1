from rich.console import *
from rich.table import *
from utils import *

console = Console()

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

def menu():
    while True:
        table = Table(title="Escolha uma opção")

        table.add_column("Opção", justify="right", style="cyan", no_wrap=True)
        table.add_column("Descrição", style="magenta")

        table.add_row("1", "Cadastrar Pessoa")
        table.add_row("2", "Cadastrar Cliente")
        table.add_row("3", "Cadastrar Atendente")
        table.add_row("4", "Cadastrar Técnico")
        table.add_row("5", "Consultar Pessoas")
        table.add_row("6", "Consultar Clientes")
        table.add_row("7", "Consultar Atendentes")
        table.add_row("8", "Consultar Técnicos")
        table.add_row("9", "Sair")

        console.print(table)

        try:
            opcao = int(input("Opção: "))
            funcao = opcoes_menu.get(opcao)
            if funcao:
                funcao()
            else:
                console.print("[red]Opção inválida![/red]")
        except ValueError:
            console.print("[red]Por favor, insira um número válido.[/red]")

if __name__ == "__main__":
    menu()

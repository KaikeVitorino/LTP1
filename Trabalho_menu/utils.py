from classes import Pessoas, Cliente, Atendente, Tecnico

def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    pessoa = Pessoas(nome, idade, sexo, cpf)
    pessoa.gravar_pessoa()

def cadastrar_cliente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    num_cliente = input("Número do Cliente: ")
    tipo_cliente = input("Tipo de Cliente: ")
    cliente = Cliente(nome, idade, sexo, cpf, num_cliente, tipo_cliente)
    cliente.gravar_cliente()

def cadastrar_atendente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    num_atendente = input("Número do Atendente: ")
    data_contratacao = input("Data de Contratação: ")
    atendente = Atendente(nome, idade, sexo, cpf, num_atendente, data_contratacao)
    atendente.gravar_atendente()

def cadastrar_tecnico():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    num_tecnico = input("Número do Técnico: ")
    especialidade = input("Especialidade: ")
    data_contratacao = input("Data de Contratação: ")
    tecnico = Tecnico(nome, idade, sexo, cpf, num_tecnico, especialidade, data_contratacao)
    tecnico.gravar_tecnico()

def consultar_pessoas():
    Pessoas.ler_arq_pes()

def consultar_clientes():
    Cliente.ler_arq_cli()

def consultar_atendentes():
    Atendente.ler_arq_ate()

def consultar_tecnicos():
    Tecnico.ler_arq_tec()

def sair():
    exit()

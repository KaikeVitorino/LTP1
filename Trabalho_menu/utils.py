from classes import Pessoas, Cliente, Atendente, Tecnico

# Função para cadastrar uma nova pessoa
def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    pessoa = Pessoas(nome, idade, sexo, cpf)
    pessoa.gravar_pessoa()

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    num_cliente = input("Número do Cliente: ")
    tipo_cliente = input("Tipo de Cliente: ")
    cliente = Cliente(nome, idade, sexo, cpf, num_cliente, tipo_cliente)
    cliente.gravar_cliente()

# Função para cadastrar um novo atendente
def cadastrar_atendente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    cpf = input("CPF: ")
    num_atendente = input("Número do Atendente: ")
    data_contratacao = input("Data de Contratação: ")
    atendente = Atendente(nome, idade, sexo, cpf, num_atendente, data_contratacao)
    atendente.gravar_atendente()

# Função para cadastrar um novo técnico
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

# Função para consultar as pessoas cadastradas
def consultar_pessoas():
    Pessoas.ler_arq_pes()

# Função para consultar os clientes cadastrados
def consultar_clientes():
    Cliente.ler_arq_cli()

# Função para consultar os atendentes cadastrados
def consultar_atendentes():
    Atendente.ler_arq_ate()

# Função para consultar os técnicos cadastrados
def consultar_tecnicos():
    Tecnico.ler_arq_tec()

# Função para sair do programa
def sair():
    exit()

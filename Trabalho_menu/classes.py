# Definição da classe base 'Pessoas'
class Pessoas:
    def __init__(self, nome, idade, sexo, cpf):
        # Inicializa os atributos da pessoa
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def gravar_pessoa(self):
        # Abre o arquivo 'Pessoas.txt' em modo de adição
        arq_pes = open('Pessoas.txt', 'a')
        # Escreve os dados da pessoa no arquivo
        arq_pes.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
        arq_pes.close()  # Fecha o arquivo após a escrita

    @classmethod
    def ler_arq_pes(cls):
        # Abre o arquivo 'Pessoas.txt' em modo de leitura
        f = open('Pessoas.txt', 'r')
        print('|~~~~~~~| Leitura de pessoa |~~~~~~~|')
        l = f.read()  # Lê o conteúdo do arquivo
        print(f"{l}\n")  # Imprime o conteúdo lido
        f.close()  # Fecha o arquivo após a leitura


# Definição da classe 'Cliente', derivada de 'Pessoas'
class Cliente(Pessoas):
    def __init__(self, nome, idade, sexo, cpf, num_cliente, tipo):
        # Chama o construtor da classe base
        super().__init__(nome, idade, sexo, cpf)
        self.tipo = tipo
        self.num_cliente = num_cliente

    def gravar_cliente(self):
        # Abre o arquivo 'Clientes.txt' em modo de adição
        arq_cli = open('Clientes.txt', 'a')
        # Escreve os dados do cliente no arquivo
        arq_cli.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" Tipo de cliente: {self.tipo}\n"
                      f" numero: {self.num_cliente}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
        arq_cli.close()  # Fecha o arquivo após a escrita

    @classmethod
    def ler_arq_cli(cls):
        # Abre o arquivo 'Clientes.txt' em modo de leitura
        f = open('Clientes.txt', 'r')
        print('|~~~~~~~| Leitura de cliente |~~~~~~~|')
        l = f.read()  # Lê o conteúdo do arquivo
        print(f"{l}\n")  # Imprime o conteúdo lido
        f.close()  # Fecha o arquivo após a leitura


# Definição da classe 'Atendente', derivada de 'Pessoas'
class Atendente(Pessoas):
    def __init__(self, nome, idade, sexo, cpf, num_atendente, data_contratacao):
        # Chama o construtor da classe base
        super().__init__(nome, idade, sexo, cpf)
        self.num_ate = num_atendente
        self.data_contratacao = data_contratacao

    def gravar_atendente(self):
        # Abre o arquivo 'Atendentes.txt' em modo de adição
        arq_ate = open('Atendentes.txt', 'a')
        # Escreve os dados do atendente no arquivo
        arq_ate.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" numero: {self.num_ate}\n"
                      f" Data de contratação: {self.data_contratacao}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
        arq_ate.close()  # Fecha o arquivo após a escrita

    @classmethod
    def ler_arq_ate(cls):
        # Abre o arquivo 'Atendentes.txt' em modo de leitura
        f = open('Atendentes.txt', 'r')
        print('|~~~~~~~| Leitura de atendente |~~~~~~~|')
        l = f.read()  # Lê o conteúdo do arquivo
        print(f"{l}\n")  # Imprime o conteúdo lido
        f.close()  # Fecha o arquivo após a leitura


# Definição da classe 'Tecnico', derivada de 'Pessoas'
class Tecnico(Pessoas):
    def __init__(self, nome, idade, sexo, cpf, num_tecnico, especialidade, data_contratacao):
        # Chama o construtor da classe base
        super().__init__(nome, idade, sexo, cpf)
        self.num_tecnico = num_tecnico
        self.data_contratacao = data_contratacao
        self.especialidade = especialidade

    def gravar_tecnico(self):
        # Abre o arquivo 'Tecnicos.txt' em modo de adição
        arq_tec = open('Tecnicos.txt', 'a')
        # Escreve os dados do técnico no arquivo
        arq_tec.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" numero: {self.num_tecnico}\n"
                      f" Data de contratação: {self.data_contratacao}\n"
                      f" Especialidade tecnica: {self.especialidade}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
        arq_tec.close()  # Fecha o arquivo após a escrita

    @classmethod
    def ler_arq_tec(cls):
        # Abre o arquivo 'Tecnicos.txt' em modo de leitura
        f = open('Tecnicos.txt', 'r')
        print('|~~~~~~~| Leitura de tecnico |~~~~~~~|')
        l = f.read()  # Lê o conteúdo do arquivo
        print(f"{l}\n")  # Imprime o conteúdo lido
        f.close()  # Fecha o arquivo após a leitura

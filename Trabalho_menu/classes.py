class Pessoas:
    def __init__(self, nome, idade, sexo, cpf):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def gravar_pessoa(self):
        arq_pes = open('Pessoas.txt', 'a')
        arq_pes.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    @classmethod
    def ler_arq_pes(self):
        f = open('Pessoas.txt', 'r')
        print('|~~~~~~~| Leitura de pessoa |~~~~~~~|')
        l = f.read()
        print(f"{l}\n")


class Cliente(Pessoas):
    def __init__(self,  nome, idade, sexo, cpf, num_cliente, tipo):
        super().__init__(nome, idade, sexo, cpf)
        self.tipo = tipo
        self.num_cliente = num_cliente

    def gravar_cliente(self):
        arq_cli = open('Clientes.txt', 'a')
        arq_cli.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" Tipo de cliente: {self.tipo}\n"
                      f" numero: {self.num_cliente}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    @classmethod
    def ler_arq_cli(self):
        f = open('Clientes.txt', 'r')
        print('|~~~~~~~| Leitura de cliente |~~~~~~~|')
        l = f.read()
        print(f"{l}\n")


class Atendente(Pessoas):
    def __init__(self, nome, idade, sexo, cpf, num_atendente, data_contratacao):
        super().__init__(nome, idade, sexo, cpf)
        self.num_ate = num_atendente
        self.data_contratacao = data_contratacao

    def gravar_atendente(self):
        arq_ate = open('Atendentes.txt', 'a')
        arq_ate.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" numero: {self.num_ate}\n"
                      f" Data de contratação: {self.data_contratacao}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    @classmethod
    def ler_arq_ate(self):
        f = open('Atendentes.txt', 'r')
        print('|~~~~~~~| Leitura de atendente |~~~~~~~|')
        l = f.read()
        print(f"{l}\n")


class Tecnico(Pessoas):
    def __init__(self, nome, idade, sexo, cpf, num_tecnico, especialidade, data_contratacao):
        super().__init__(nome, idade, sexo, cpf)
        self.num_tecnico = num_tecnico
        self.data_contratacao = data_contratacao
        self.especialidade = especialidade

    def gravar_tecnico(self):
        arq_tec = open('Tecnicos.txt', 'a')
        arq_tec.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f" Idade: {self.idade}\n"
                      f" sexo:{self.sexo}\n"
                      f" numero: {self.num_tecnico}\n"
                      f" Data de contratação: {self.data_contratacao}\n"
                      f" Especialidade tecnica: {self.especialidade}\n"
                      f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    @classmethod
    def ler_arq_tec(self):
        f = open('Tecnicos.txt', 'r')
        print('|~~~~~~~| Leitura de tecnico |~~~~~~~|')
        l = f.read()
        print(f"{l}\n")





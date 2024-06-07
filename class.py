import datetime

class Pessoa:
    def __init__(self, nome, peso, altura, ano_nascimento=2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if len(novo_nome) > 2:
            self.nome = novo_nome
        else:
            self.nome = "Dados inconsistentes"

    def get_peso(self):
        return self.peso

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def get_altura(self):
        return self.altura

    def set_altura(self, nova_altura):
        self.altura = nova_altura

    def get_ano_nascimento(self):
        return self.ano_nascimento

    def set_ano_nascimento(self, novo_ano_nascimento):
        self.ano_nascimento = novo_ano_nascimento

    def imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc

    def __str__(self):
        return f'Nome: {self.nome} ,Peso: {self.peso} ,Altura: {self.altura} ,Ano de nascimento: {self.ano_nascimento})'

    def calcula_idade(self):
        data = datetime.date.today()
        idade = data.year - self.ano_nascimento
        return idade

    def retorna_mais_velho(self, pessoa):
        if self.ano_nascimento > pessoa.get_ano_nascimento():
            return f' {self.nome} é mais velho que {pessoa.get_nome()} '
        else:
            return f' {pessoa.get_nome()} é mais velho que {self.nome} '


if __name__ == '__main__':
    pessoa1 = Pessoa('Eduardo', 70, 2.00, 2002)
    pessoa2 = Pessoa('Luã', 50, 1.50, 2004)
    pessoa3 = Pessoa('Carlos', 80, 1.80, 2002)
    print("Nome:",pessoa1.get_nome())
    pessoa1.set_nome('Eduarda')
    print("Novo nome:", pessoa1.get_nome())
    print("Peso:",pessoa1.get_peso())
    print("Altura:",pessoa1.get_altura())
    print("Ano de nascimento:",pessoa1.get_ano_nascimento())
    pessoa1.set_ano_nascimento(2000)
    print("Novo ano de nascimento:", pessoa1.get_ano_nascimento())
    print("IMC:", pessoa1.imc())
    print("Ficha:",pessoa1)
    print("Idade:",pessoa1.calcula_idade())

    print("Nome:",pessoa2.get_nome())
    print("Peso:",pessoa2.get_peso())
    print("Altura:",pessoa2.get_altura())
    print("Ano de nascimento:",pessoa2.get_ano_nascimento())
    print("IMC:", pessoa2.imc())
    print("Ficha:",pessoa2)
    print("Idade:",pessoa2.calcula_idade())

    print("Nome:",pessoa3.get_nome())
    print("Peso:",pessoa3.get_peso())
    print("Altura:",pessoa3.get_altura())
    print("Ano de nascimento:",pessoa3.get_ano_nascimento())
    print("IMC:", pessoa3.imc())
    print("Ficha:",pessoa3)
    print("Idade:",pessoa3.calcula_idade())

    print(pessoa1.mais_velho(pessoa2))

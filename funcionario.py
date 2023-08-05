class funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_horas = {}

    def cadastro_hora(self,mes, hora):
        if (mes not in self.horas):
            self.horas[mes] = hora

    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_horas):
         self.salario_horas[mes] = valor

    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_horas):
            print('Mês Inexistente')
        else:
            return self.horas[mes] * self.salario_horas[mes]

    def __repr__(self):
        return f'funcionário: {self.nome}, \nEmail: {self.email}, \nhoras/mês: {self.horas},\nsalário-horas: {self.salario_horas}'

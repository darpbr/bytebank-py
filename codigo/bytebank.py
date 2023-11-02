from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario
    
    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_separado = nome_completo.split(' ')
        return nome_separado[-1]

    def idade(self):
        data_nascimento_separada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_separada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor
    
    def _eh_socio(self):
        sobrenomes = ['Braganca', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self.salario >= 100000) and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
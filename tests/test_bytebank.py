import pytest
from pytest import mark
from codigo.bytebank import Funcionario

class TestClass:
    """Classe de Testes da função principal
    """
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        """Teste de idade
        """
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste',entrada, 1000)

        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        """Teste de Sobrenome do funcionário
        """
        entrada = 'Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000',1000)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quando_nome_recebe_lucas_carvalho_deve_retornar_Lucas_Carvalho(self):
        """Teste de Sobrenome do funcionário
        """
        entrada = 'Lucas Carvalho'
        esperado = 'Lucas Carvalho'

        lucas = Funcionario(entrada, '11/11/2000',1000)
        resultado = lucas.nome

        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100_mil_deve_retornar_90_mil(self):
        """teste da funcionalidade de decrescimo de salario
        """
        entrada_salario = 100000 # given
        entrada_nome = 'Paulo Braganca'
        esperado = 90000 

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when

        resultado = funcionario_teste.salario

        assert resultado == esperado # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        """teste da funcionalidade que calcula o bônus
        """
        entrada_salario = 1000 # given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        """teste de exception quando 10% do salário for maior que R$ 1.000,00
        """
        with pytest.raises(Exception):
            entrada_salario = 10000000 # given

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus() # when

            assert resultado # then

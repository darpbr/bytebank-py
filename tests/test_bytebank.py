from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'
        esperado = 23
        
        funcionario_teste = Funcionario('Teste',entrada, 1000)
        
        resultado = funcionario_teste.idade()
        
        assert resultado == esperado
    
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvahlo(self):
        entrada = 'Lucas Carvalho '
        esperado = 'Carvalho'
        
        lucas = Funcionario(entrada, '11/11/2000',1000)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado
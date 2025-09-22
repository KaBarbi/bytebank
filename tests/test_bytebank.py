from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_22_11_2000_deve_retornar_25(self):
        entrada = '22/11/2000'
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_nome_recebe_kleber_silva_deve_retornar_silva(self):
        entrada = ' Kleber Silva '
        esperado = 'Silva'

        kleber = Funcionario(entrada, '11/11/2000', 1111)

        resultado = kleber.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_nome = 'Paulo Bragança'
        entrada_salario = 100000
        esperado = 90000

        funcionario_test = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario

        assert resultado == esperado

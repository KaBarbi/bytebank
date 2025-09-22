from codigo.bytebank import Funcionario

# kleber = Funcionario('Kleber Silva', '22/11/2000', 1000)
# print(kleber.idade())


def teste_idade():
    funcionario_teste = Funcionario('tete', '22/11/2000', 1111)
    print(f'teste = {funcionario_teste.idade()}')

teste_idade()
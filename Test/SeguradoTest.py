from DAO.SeguradoDAO import DAOSegurado
from datetime import date

dao=DAOSegurado.Segurado()
def testeLer():

    for c in dao.readAll():
        print(str(c.COD)+" "+c.NOME+" ")
def testeLerUnico():
    pessoas=dao.readById(65556)
    print("COD: " + str(pessoas.COD) + " NOME: " + pessoas.NOME)
def testeBuscarNome():
    nome = "Pedro"
    segurado=dao.readByName(nome)
    for c in segurado:
        print("COD: "+str(c.COD)+" Nome: "+c.NOME)
def testeAdicionar():
    novoSegurado=dao.segurado()

    novoSegurado.NOME="Nilton Teste"
    novoSegurado.CPF="12345678911"
    novoSegurado.RG="123456"
    novoSegurado.PROFISSAO="Trabalhador"
    novoSegurado.EMPRESA="TCU"
    novoSegurado.RENDA=23.50
    novoSegurado.OBSERVACAO="É apenas um teste de inserção"
    novoSegurado.DATA_NASCIMENTO=date(2023,7,22)

    dao.create(novoSegurado)
def testeAlterar():
    pessoa=dao.readById(6557)
    pessoa.NOME="Zé do Teste"
    dao.update()
def testeExcluir():
    pessoa=dao.readById(6556)
    dao.delete(pessoa)
#testeAdicionar() #OK
#testeLer() #OK
testeBuscarNome() #OK
#testeLerUnico() #OK
#testeAlterar() #OK
#testeExcluir() #OK
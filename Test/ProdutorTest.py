from DAO.ProdutorDAO import ProdutorDAO
from datetime import date

dao=ProdutorDAO.Produtor()

def testeAdicionar():
    produtorNovo=dao.produtor()

    produtorNovo.NOME='Serjão Foguetes'

    dao.create(produtorNovo)

def testeLer():
    produtores=dao.readAll()
    for c in produtores:
        print("{ COD: "+str(c.COD)+' NOME: '+c.NOME+"}")
def testeLerUnico():
    produtor=dao.readByID(27)
    print("COD: "+str(produtor.COD)+" NOME: "+produtor.NOME)
def testeBuscarNome():
    nome="AN"
    pessoas=dao.readByName(nome)
    for c in pessoas:
        print(str(c.COD)+" "+c.NOME)
def testeAlterar():
    pessoa=dao.readByID(27)
    pessoa.NOME="Homem Cordial"
    dao.update()
def testeExcluir():
    pessoa_excluida=dao.readByID(27)
    dao.delete(pessoa_excluida)

#testeAdicionar()
testeLer()
#testeBuscarNome()
#testeLerUnico()
#testeAlterar()
#testeExcluir()
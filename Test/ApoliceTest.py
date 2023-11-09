from DAO.ApoliceDAO import DAOApolice
from datetime import date

dao=DAOApolice.Apolice()
def testeLer():
    apolices=dao.readAll()
    for c in apolices:
        print(str(c.COD)+" Seguradora: "+c.SEGURADORA+" Produto: "+str(c.PRODUTO))
def testeAdicionar():
    novaApolice=dao.apolice()

    novaApolice.SEGURADORA="LIBERTY"
    novaApolice.RAMO="AUTO"
    novaApolice.INIVIGOR=date(2023,9,28)
    novaApolice.FIMVIGOR=date(2024,9,29)
    novaApolice.PRODUTO="Carro de teste"
    novaApolice.COD_PRODUTOR=1
    novaApolice.COD_SEGURADO=6555
    novaApolice.premio_liquido=232.9
    novaApolice.premio_total=500

    dao.create(novaApolice)
def testeLerUnico():
    apolice=dao.readByID(762)
    print("FIMVIGOR: "+str(apolice.FIMVIGOR)+" mes: "+str(apolice.FIMVIGOR.month))
    print("COD: "+str(apolice.COD)+" Seguradora: "+apolice.SEGURADORA+" COD_PRODUTOR: "+
          str(apolice.COD_PRODUTOR)+" premio_liquido: "+str(apolice.premio_liquido))

def testeExcluir():
    apolice=dao.readById(10036)
    dao.delete(apolice)

def testeAlterar():
    apolice=dao.readById(10036)
    apolice.premio_liquido=0.0
    dao.update()
def testeListarApolicesMES():
    APOLICES=dao.listaApolicesVencendo("08")

    for c in APOLICES:
        print("COD: "+str(c.COD)+" FIMVIGOR: "+str(c.FIMVIGOR))

#testeAdicionar() #OK
#testeLer() #OK
#testeBuscarNome() #Essa função não tem na apolice, farei de outro jeito
testeLerUnico() #OK
#testeAlterar() #OK
#testeExcluir() #OK
#testeListarApolicesMES()#OK

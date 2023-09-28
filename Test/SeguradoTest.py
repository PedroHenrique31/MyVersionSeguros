from DAO.SeguradoDAO import DAOSegurado
from datetime import date

dao=DAOSegurado.Segurado()
def testeLer():

    for c in dao.readAll():
        print(str(c.COD)+" "+c.NOME+" ")


#testeAdicionar()
testeLer()
#testeBuscarNome()
#testeLerUnico()
#testeAlterar()
#testeExcluir()

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
    nome = "IANO"
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
def testeTelefone():
    id=5857
    segurado=dao.readByID(id)
    telefones=dao.readTelefone(id)
    print("Nome: "+segurado.NOME+" trabalha em: "+str(segurado.EMPRESA)+"\ntelefones: ",end="")
    for c in telefones:
        if(c.TELEFONE!=None):
            print("("+c.DDD+") "+c.TELEFONE+" ",end="")
        else:
            print("Não tem telefone na lista")
    print("\n")
def testeEndereco():
    id=5662
    segurado=dao.readByID(id)
    telefones=dao.readEnderecos(id)
    print("Nome: "+segurado.NOME+" trabalha em: "+str(segurado.EMPRESA)+"\nendereços: ",end="")
    for c in telefones:
        if(c.ENDERECO!=None):
            print(c.ENDERECO+" ",end="")
            print(" | ",end="")
        else:
            print("Não tem endereço na lista")
    print("\n")
def testeEmail():
    id=5662
    segurado=dao.readByID(id)
    telefones=dao.readEmail(id)
    print("Nome: "+segurado.NOME+" trabalha em: "+str(segurado.EMPRESA)+"\ne-mails: ",end="")
    for c in telefones:
        if(c.EMAIL!=None):
            print(c.EMAIL+" ",end="")
            print(" | ",end="")
        else:
            print("Não tem endereço na lista")
    print("\n")

#testeAdicionar() #OK
testeLer() #OK
testeBuscarNome() #OK
#testeLerUnico() #OK
#testeAlterar() #OK
#testeExcluir() #OK
testeTelefone() #OK
testeEndereco() #OK
testeEmail()#OK
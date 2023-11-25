"""
            Classe DAO Segurado
        Nessa classe vamos acessar e manipular dados das tabelas de Segurado e
    de suas tabelas correlatas tais como: endereço,email e telefone.

    author:Pedro Henrique Carneiro de Araújo
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class Segurado:
    def __init__(self):
        engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/myversion_cawa_model?charset=utf8mb4")
        DB = automap_base()
        DB.prepare(engine, reflect=True)

        self.segurado = DB.classes.segurado
        self.endereco = DB.classes.endereco
        self.telefone = DB.classes.telefone
        self.email = DB.classes.email
        self.apolice= DB.classes.apolice

        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()
    def readAllTelefoneToo(self):
        consulta=self.ses.query(self.segurado,self.telefone.DDD,self.telefone.TELEFONE).\
            join(self.telefone).filter(self.segurado.COD==self.telefone.COD_SEGURADO).all()
        return consulta
    # Lista telefones de um determinado segurado
    def readTelefone(self,id_segurado):
        telefones=self.ses.query(self.telefone).filter_by(COD_SEGURADO=id_segurado).all()
        return telefones
    #Lista apolices de um determinado segurado
    def readApolice(self,id_segurado):
        consulta=self.ses.query(self.apolice).filter_by(COD_SEGURADO=id_segurado).all()
        return consulta
    # Lista endereços de um determinado segurado
    def readEnderecos(self,id_segurado):
        enderecos=self.ses.query(self.endereco).filter_by(COD_SEGURADO=id_segurado)
        return enderecos
    # Lista emails de um determinado segurado
    def readEmail(self,id_segurado):
        emails=self.ses.query(self.email).filter_by(COD_SEGURADO=id_segurado)
        return emails
    # Lista todos os segurados
    def readAll(self):
        segurados=self.ses.query(self.segurado).limit(200).all()
        return segurados
    # Acessa um segurado pelo seu ID
    def readByID(self,id):
        segurado= self.ses.query(self.segurado).filter_by(COD=id).first()
        return  segurado
    def create(self,segurado):
        self.ses.add(segurado)
        self.ses.commit()
    #Adiciona os dados de outras tabelas
    def createTelefone(self,telefone):
        self.ses.add(telefone)
        self.ses.commit()
    def createEndereco(self,endreceo):
        self.ses.add(endreceo)
        self.ses.commit()
    def createEmail(self,email):
        self.ses.add(email)
        self.ses.commit()
    #Altera dados de segurado
    def update(self):
        self.ses.commit()
    def delete(self,segurado):
        self.ses.delete(segurado)
        self.ses.commit()
    def __del__(self):
        self.ses.close()
    # retorna uma lista de segurados buscando-os pelo nome
    def readByName(self,nome):
        segurados=self.ses.query(self.segurado).filter(self.segurado.NOME.ilike('%'+nome+'%')).all()
        return segurados
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
        #Não sei se adiciono uma tabela de apolices.

        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()
    def readAllTelefoneToo(self):
        consulta=self.ses.query(self.segurado,self.telefone.DDD,self.telefone.TELEFONE).\
            join(self.telefone).filter(self.segurado.COD==self.telefone.COD_SEGURADO).all()
        return consulta
    def readAll(self):
        segurados=self.ses.query(self.segurado).all()
        return segurados
    def readById(self,id):
        segurado=self.ses.query(self.segurado).filter_by(COD=id).first()
        return  segurado
    def create(self,segurado):
        self.ses.add(segurado)
        self.ses.commit()
    def update(self):
        self.ses.commit()
    def delete(self,segurado):
        self.ses.delete(segurado)
        self.ses.commit()
    def __del__(self):
        self.ses.close()
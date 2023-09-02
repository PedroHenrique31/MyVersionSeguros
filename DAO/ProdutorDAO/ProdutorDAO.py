from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class Produtor:
    def __init__(self):
        engine=create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/myversion_cawa_model?charset=utf8mb4")
        DB=automap_base()
        DB.prepare(engine,reflect=True)
        self.produtor=DB.classes.produtor
        session_factory=sessionmaker(bind=engine)
        self.ses=session_factory()
# ------------- Operações no BD --------------------
    # cria um novo produtor
    def create(self, produtor):
        self.ses.add(produtor)
        self.ses.commit()
    # Lista todas as apólices de seguro
    def readAll(self):
        apolices=self.ses.query(self.produtor).all()
        return apolices
    # mostra uma apólice específica pelo ID_SEGURO
    def readByID(self,id):
        produtor = self.ses.query(self.produtor).filter_by(COD=id).first()
        return produtor
    def readByName(self,nome):
        produtores=self.ses.query(self.produtor).filter(self.produtor.NOME.ilike('%' + nome + '%')).all()
        return produtores

    def update(self):
        self.ses.commit()
    def delete(self,produtor):
        self.ses.delete(produtor)
        self.ses.commit()
    def __del__(self):
        self.ses.close()
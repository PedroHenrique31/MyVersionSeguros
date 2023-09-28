from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class Apolice:
    def __init__(self):
        engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/myversion_cawa_model?charset=utf8mb4")
        DB = automap_base()
        DB.prepare(engine, reflect=True)

        self.apolice=DB.classes.apolice
        self.produtor=DB.classes.produtor
        self.segurado=DB.classes.segurado

        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()

    def readAll(self):
        apolices=self.ses.query(self.apolice).all()
        return apolices
    def readById(self,id):
        apolice = self.ses.query(self.apolice).filter_by(COD=id).first()
        return apolice
    def create(self,apolice):
        self.ses.add(apolice)
        self.ses.commit()
    def update(self):
        self.ses.commit()
    def delete(self,apolice):
        self.ses.delete(apolice)
        self.ses.commit()
    def __del__(self):
        self.ses.close()
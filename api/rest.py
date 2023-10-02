"""
            Módulo REST

        Nesse módulo vamos usar o framework flask_RESTful para implementar uma API que
    permita o acesso aos dados.
        Assim, nesse arquivo vamos implementar os verbos GET,POST,PUT,DELETE
    e usar as classes DAO já criadas para performar consultas e alterações nos dados do
    banco de dados da CAWA.
        Nessa classe em geral vamos converter os dados oriundos das classes DAO, e
    serializá-los, em outros termos, converter para JSON, assim o flask pode pegar o JSON
    e gerar um HTML como resposta para ser enviada para o usuário, ela também necessita
    realizar o processo reverso, chamado desserialização, de ler uma solicitação HTML e
    gerar um JSON correspondente que vai ser processado e levado a classe DAO para ser
    utilizado no BD.



    author:Pedro Henrique Carneiro de Araújo
"""
from flask_restful import Resource, request
from flask import jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from DAO.ProdutorDAO import ProdutorDAO # Importamos o pacote e pacote do pacote após isso o arquivo ProdutorDAO
from DAO.SeguradoDAO import DAOSegurado
from DAO.ApoliceDAO import DAOApolice

# Cria classes de acesso ao BD, para manipular as tabelas de produtor,segurado e apolices.
dados_Produtor=ProdutorDAO.Produtor()
dados_Segurado=DAOSegurado.Segurado()
dados_Apolice=DAOApolice.Apolice()

"""
    Cria classes de esquema, essas classes servem para declararmos os 
modelos de dados a serem manipulados no BD, com isso ao declararmos as 
classes Meta e passarmos uma tabela do BD como model, o SQLAlchemySchema 
vai saber os campos que temos na tabela e com isso pode serializar e 
desserializar os objetos do BD.
"""
class ProdutorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dados_Produtor.produtor
class SeguradoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dados_Segurado.segurado
class ApoliceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dados_Apolice.apolice

"""
    Cria classes de recursos REST, nessas classes criamos os 
recursos que vamos utilizar para responder as solicitações HTTP
vindos do usuário, e serializamos e desserializamos.
nela usamos as classes dao e implementamos respostas aos verbos:
    -get;
    -post;
    -put;
    -delete;
"""
class ProdutorRest(Resource):
    def __init__(self):
        self.campos=['COD','NOME']
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
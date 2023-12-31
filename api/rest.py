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
import os
from flask_restful import Resource, request
from flask import jsonify,send_file
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from DAO.ProdutorDAO import ProdutorDAO # Importamos o pacote e pacote do pacote após isso o arquivo ProdutorDAO
from DAO.SeguradoDAO import DAOSegurado
from DAO.ApoliceDAO import DAOApolice
from datetime import datetime

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
        fields = ('COD','SEGURADORA','RAMO','INIVIGOR','FIMVIGOR','PRODUTO',
                     'LINK_APOLICE','COD_PRODUTOR','PRODUTOR_NOME','COD_SEGURADO','premio_liquido',
                     'premio_total')

"""
    Cria classes de recursos REST, nessas classes criamos os 
recursos que vamos utilizar para responder as solicitações HTTP
vindos do usuário, e serializamos e desserializamos.
nela usamos as classes dao e implementamos respostas aos verbos:
    -get: Lê dados;
    -post: Cria um novo elemento;
    -put: Atualiza os dados;
    -delete: Exclui dados.
"""
class ProdutorRest(Resource):
    def __init__(self):
        self.campos=['COD','NOME']
    # Lê dados do BD
    def get(self):
        ## Se a solicitação de get passar como argumento o campo COD, chama a função readByID
        if request.args.get(self.campos[0]) is not None:
            id_produtor=request.args.get(self.campos[0])
            obj=dados_Produtor.readByID(id_produtor)
            schema=ProdutorSchema() # cria um schema com a tabela produtor
            algo=schema.dump(obj) # converte o obj consultado em um troço, provavelmente num hash
            return jsonify(algo) # gera um json a partir de algo e envia de volta, encerrando a função.
        ## Se a solicitação passar como argumento o campo NOME, chama a função readByName.
        elif request.args.get("NOME") is not None:
            lista = dados_Produtor.readByName(request.args.get("NOME")) # consulta por nome
            schema=ProdutorSchema(many=True) # chama a classe esquema avisando que haverá uma lista de dados a serem formatados.
            return jsonify(schema.dump(lista)) # gera o JSON da lista toda.
        ## Se a solicitação não passar nenhum argumento, chama a função readAll.
        else:
            lista=dados_Produtor.readAll()
            schema=ProdutorSchema(many=True)
            return jsonify(schema.dump(lista))
    # Cria um novo elemento no BD.
    def post(self):
        obj=dados_Produtor.produtor() # cria um objeto do tipo produtor
        obj.NOME=request.args.get("NOME")
        dados_Produtor.create(obj)
        return jsonify({'insert':obj.COD})
    # Atualiza dados no BD.
    def put(self):
        obj = dados_Produtor.readByID(request.args.get(self.campos[0]))
        if obj is None:
            return jsonify({'update':0})
        else:
            for c in self.campos:
                if request.args.get(c) is not None:
                    exec('obj.{} =request.args.get("{}")'.format(c, c))
                    dados_Produtor.update()
                    return jsonify({'update':obj.COD})
    # Exclui dados no BD.
    def delete(self):
        id=request.args.get(self.campos[0])
        obj = dados_Produtor.readByID(id)
        if obj is None:
            return jsonify({"delete":0})
        else:
            dados_Produtor.delete(obj)
            return jsonify({"delete":id})
######################################################################################################
class ApoliceRest(Resource):
    def __init__(self):
        self.campos=['COD','SEGURADORA','RAMO','INIVIGOR','FIMVIGOR','PRODUTO',
                     'LINK_APOLICE','COD_PRODUTOR','COD_SEGURADO','premio_liquido',
                     'premio_total']

    # Lê dados do BD
    def get(self):
        ## Se a solicitação de get passar como argumento o campo COD, chama a função readByID
        if request.args.get(self.campos[0]) is not None:
            id_apolice=request.args.get(self.campos[0])
            obj=dados_Apolice.readByID(id_apolice)
            schema=ApoliceSchema() # cria um schema com a tabela apolice
            algo=schema.dump(obj) # converte o obj consultado em um troço, provavelmente num dicionario
            #cod_produtor=algo['COD_PRODUTOR']
            nome_produtor=obj.produtor.NOME
            nome_segurado=obj.segurado.NOME
            algo['PRODUTOR_NOME']=nome_produtor
            algo['SEGURADO_NOME']=nome_segurado
            return jsonify(algo) # gera um json a partir de algo e envia de volta, encerrando a função.
        ## Se a solicitação passar como argumento algum campo conhecido de pesquisa.
        elif request.args.get("MESVENCIMENTO") is not None:
            lista =[]
            mesVencimento=request.args.get("MESVENCIMENTO")
            lista=dados_Apolice.listaApolicesVencendo(mesVencimento)
            schema=ApoliceSchema(many=True)
            algo=schema.dump(lista)
            print("entrou na busca por apolices vencendo")
            return jsonify(algo)

        ## Se a solicitação não passar nenhum argumento, chama a função readAll.
        else:
            lista=dados_Apolice.readAll()
            schema=ApoliceSchema(many=True)
            return jsonify(schema.dump(lista))

    # Cria um novo elemento no BD.
    def post(self):
        obj=dados_Apolice.apolice() # cria um objeto do tipo apolice
        for c in self.campos:
            if c!='COD':
                exec("obj.{}=request.args.get('{}')".format(c,c))
        dados_Apolice.create(obj)
        return jsonify({'insert':obj.COD})

    # Atualiza dados no BD.
    def put(self):
        obj = dados_Apolice.readByID(request.args.get(self.campos[0]))
        if obj is None:
            return jsonify({'update':0})
        else:
            for c in self.campos:
                if request.args.get(c) is not None:
                    exec('obj.{}=request.args.get("{}")'.format(c, c))
                    dados_Apolice.update()
                    return jsonify({'update':obj.COD})

    # Exclui dados no BD.
    def delete(self):
        id=request.args.get(self.campos[0])
        obj = dados_Apolice.readByID(id)
        if obj is None:
            return jsonify({"delete":0})
        else:
            dados_Apolice.delete(obj)
            return jsonify({"delete":id})

#########################################################################################################
class SeguradoRest(Resource):
    def __init__(self):
        self.campos=['COD','NOME','CPF','RG','PROFISSAO','EMPRESA',
                     'RENDA','OBSERVACAO','DATA_NASCIMENTO']
        self.camposEmail=['COD','EMAIL','COD_SEGURADO']
        self.camposTelefone=['COD','TELEFONE','DDD','NOTAS','COD_SEGURADO']
        self.camposEndereco=['COD','ENDERECO','TIPO','BAIRRO','CIDADE','UF','CEP','COD_SEGURADO']

    # Lê dados do BD
    def get(self):
        ## Se a solicitação de get passar como argumento o campo COD, chama a função readByID
        if request.args.get(self.campos[0]) is not None:
            id_segurado=request.args.get(self.campos[0])
            obj=dados_Segurado.readByID(id_segurado)
            schema=SeguradoSchema() # cria um schema com a tabela apolice
            algo=schema.dump(obj) # converte o obj consultado em um troço, provavelmente num hash
            # Busca telefones,emails e endereços da pessoa
            tels=dados_Segurado.readTelefone(id_segurado)
            OBJemails=dados_Segurado.readEmail(id_segurado)
            OBJenderecos=dados_Segurado.readEnderecos(id_segurado)
            OBJapolices=dados_Segurado.readApolice(id_segurado)
            # Processa as informações
            telefones=[{"DDD":tel.DDD,"FONE":tel.TELEFONE,"COD":tel.COD} for tel in tels]
            emails=[{"COD":e.COD,"EMAIL":e.EMAIL} for e in OBJemails]
            enderecos=[{"COD":end.COD,"ENDERECO":end.ENDERECO,"TIPO":end.TIPO,"BAIRRO":end.BAIRRO,
                            "CIDADE":end.CIDADE,"UF":end.UF,"CEP":end.CEP} for end in OBJenderecos]
            apolices=[{"COD":ap.COD,"SEGURADORA":ap.SEGURADORA,"RAMO":ap.RAMO,"PREMIO_LIQUIDO":ap.premio_liquido} for ap in OBJapolices]
            # Adiciona os telefones, emails e endereços
            algo["TELEFONES"]=telefones
            algo["EMAILS"]=emails
            algo["ENDERECOS"]=enderecos
            algo["APOLICES"]=apolices
            return jsonify(algo) # gera um json a partir de algo e envia de volta, encerrando a função.
        ## Se a solicitação passar como argumento algum campo conhecido de pesquisa.
        elif request.args.get("NOME") is not None:
            lista =dados_Segurado.readByName(request.args.get("NOME")) # consulta por nome
            schema=SeguradoSchema(many=True) # chama a classe esquema avisando que haverá uma lista de dados a serem formatados.
            return jsonify(schema.dump(lista)) # gera o JSON da lista toda.

        ## Se a solicitação não passar nenhum argumento, chama a função readAll.
        else:
            lista=dados_Segurado.readAll()
            schema=SeguradoSchema(many=True)
            return jsonify(schema.dump(lista))

    # Cria um novo elemento no BD.
    def post(self):
        # Verifica se o conteúdo da requisição é JSON
        if request.is_json:
            data = request.get_json() #Passa o JSON para dict
            #print(data['TELEFONES'])
        else:
            return jsonify({'error': 'Conteúdo da requisição deve ser JSON'}), 400
        obj=dados_Segurado.segurado() # cria um objeto do tipo segurado
        for c in self.campos:
            if c!='COD' and c!='DATA_NASCIMENTO' and c!='TELEFONES' and c!='ENDERECOS' and c!='EMAILS':
                exec("obj.{}=data['{}']".format(c,c))

        obj.DATA_NASCIMENTO = datetime.strptime(data['DATA_NASCIMENTO'],'%Y-%m-%d').date()
        dados_Segurado.create(obj)
        # Tratar aqui o que fazer quando tiverem telefones de contato e outras coisas no segurado
        ## Como eu não criei uma lista com os nomes dos campos eu tenho que atribuir manualmente.
        if 'TELEFONES' in data:
            for x in data['TELEFONES']:
                #print("("+x['DDD']+")"+x['TELEFONE'])
                telefone=dados_Segurado.telefone()
                telefone.DDD=x['DDD']
                telefone.TELEFONE=x['TELEFONE']
                telefone.COD_SEGURADO=obj.COD
                #agora é dar create em telefone
                dados_Segurado.createTelefone(telefone)
        if 'ENDERECOS' in data:
            for x in data['ENDERECOS']:
                endereco=dados_Segurado.endereco()
                endereco.ENDERECO=x['ENDERECO']
                endereco.TIPO=x['TIPO']
                endereco.BAIRRO=x['BAIRRO']
                endereco.CIDADE=x['CIDADE']
                endereco.UF=x['UF']
                endereco.CEP=x['CEP']
                endereco.COD_SEGURADO=obj.COD
                dados_Segurado.createEndereco(endereco)

        if 'EMAILS' in data:
            for x in data['EMAILS']:
                email=dados_Segurado.email()
                email.EMAIL=x['EMAIL']
                email.COD_SEGURADO=obj.COD
                dados_Segurado.createEmail(email)
        return jsonify({'insert':obj.COD})

    # Atualiza dados no BD.
    def put(self):
        dadosDicionario=request.get_json() #Pega um JSON e passa pra dict

        if dadosDicionario is None:
            return jsonify({'update': 0})

        print(dadosDicionario)
        obj = dados_Segurado.readByID(dadosDicionario['COD'])
        #print(obj.COD)
        # se não encontrar o segurado na tabela encerra aqui
        if obj is None:
            return jsonify({'update':0})
        else:
            # Para cada campo da lista de segurados realiza uma alteração no campo de mesmo nome
            for c in dadosDicionario:
                if c!='COD' and c!='EMAILS':
                    exec("obj.{}=dadosDicionario['{}']".format(c,c))
            # Procura no JSON se há os campos EMAILS,ENDERECOS,TELEFONES e altera-os nas tabelas
            if 'EMAILS' in dadosDicionario:
                # Para cada email em EMAILS
                for e in dadosDicionario['EMAILS']:
                    # Se o comando for para alteração de um email específico ele deve informar o codigo do email
                    if 'CODIGO_EMAIL_ALTERAR' in e:
                        print("Altera um email especifico de COD:" + str(e['CODIGO_EMAIL_ALTERAR']) +" e tipo: "+str(type(e['CODIGO_EMAIL_ALTERAR'])))
                        id_email=e['CODIGO_EMAIL_ALTERAR']
                        emailEspecifico=dados_Segurado.pegaEmail(id_email)
                        emailEspecifico.EMAIL=e['EMAIL']
                    #Se o campo passado for de deletar:
                    elif 'CODIGO_EMAIL_DELETAR' in e:
                        print("Deletaremos o e-mail de PK:"+str(e['CODIGO_EMAIL_DELETAR']))
                    #Senão insere um novo e-mail na tabela
                    else:
                        #adiciona o email na tabela EMAILS
                        print("Tem que adicionar o email"+e['EMAIL'])
                        email=dados_Segurado.email()
                        email.EMAIL=e['EMAIL']
                        email.COD_SEGURADO=obj.COD
                        dados_Segurado.createEmail(email)
            if 'TELEFONES' in dadosDicionario:
                for tel in dadosDicionario['TELEFONES']:
                    if 'CODIGO_TELEFONE_ALTERAR' in tel:
                        id_telefone=tel['CODIGO_TELEFONE_ALTERAR']
                        telEspecifico=dados_Segurado.pegaTelefone(id_telefone)
                        telEspecifico.DDD=tel['DDD']
                        telEspecifico.TELEFONE=tel['TELEFONE']
                        telEspecifico.NOTAS=tel['NOTAS']
                    elif 'CODIGO_TELEFONE_DELETAR' in tel:
                        pass
                    else:
                        #Adiciona um telefone na tabela
                        telefone=dados_Segurado.telefone()
                        telefone.DDD=tel['DDD']
                        telefone.TELEFONE=tel['TELEFONE']
                        telefone.COD_SEGURADO=obj.COD
                        dados_Segurado.createTelefone(telefone)
            if 'ENDERECOS' in dadosDicionario:
                camposEndereco=['ENDERECO','TIPO','BAIRRO','CIDADE','UF','CEP']
                for ende in dadosDicionario['ENDERECOS']:
                    if 'CODIGO_ENDERECO_ALTERAR' in ende:
                        id_endereco=ende['CODIGO_ENDERECO_ALTERAR']
                        enderecoEspecifico=dados_Segurado.pegaEndereco(id_endereco)
                        for camp in camposEndereco:
                            exec("enderecoEspecifico.{}=ende['{}']".format(camp,camp))
                        enderecoEspecifico.COD_SEGURADO=obj.COD
                    elif 'CODIGO_ENDERECO_DELETAR' in ende:
                        pass
                    else:
                        # Adiciona um endereco na tabela
                        endereco=dados_Segurado.endereco()
                        for campo in camposEndereco:
                            #print("endereco.{}=ende['{}']".format(campo,campo))
                            exec("endereco.{}=ende['{}']".format(campo,campo))
                        endereco.COD_SEGURADO=obj.COD
                        dados_Segurado.createEndereco(endereco)

            dados_Segurado.update()
            return jsonify({'update':obj.COD})

    # Exclui dados no BD.
    def delete(self):
        id=request.args.get(self.campos[0])
        id_telefone=request.args.get('TELEFONE')
        id_endereco=request.args.get('ENDERECO')
        id_email=request.args.get('EMAIL')

        obj = dados_Segurado.readByID(id)
        telefoneDel=dados_Segurado.pegaTelefone(id_telefone)
        enderecoDel=dados_Segurado.pegaEndereco(id_endereco)
        emailDel=dados_Segurado.pegaEmail(id_email)
        if obj is not None:
            dados_Segurado.delete(obj)
            return jsonify({"delete":id})
        elif telefoneDel is not None:
            dados_Segurado.delete(telefoneDel)
            return jsonify({"deleteTEL":id_telefone})
        elif enderecoDel is not None:
            dados_Segurado.delete(enderecoDel)
            return jsonify({"deleteENDERECO": id_endereco})
        elif emailDel is not None:
            dados_Segurado.delete(emailDel)
            return jsonify({"deleteTEL": id_email})
        else:
            return jsonify({"delete":0})

class PDFHandler:
    def __init__(self):
        self.pdf_directory="C:\\Users\\pedro\\Documents\\Site\\Apolice_Seguros_2023\\"
    def download_pdf(self, filename):
        pdf_path = os.path.join(self.pdf_directory, filename+".pdf")
        if os.path.exists(pdf_path) and pdf_path.endswith('.pdf'):
            return send_file(pdf_path, as_attachment=False)
        else:
            return 'Arquivo PDF não encontrado', 404

    def upload_pdf(self):
        # Função vazia para lidar com o upload de arquivos PDF
        pass
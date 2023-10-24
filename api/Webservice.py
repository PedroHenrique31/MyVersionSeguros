from flask import Flask,request,send_file
from flask_restful import Api
import rest
from rest import PDFHandler
import os

app=Flask(__name__)
api=Api(app)

api.add_resource(rest.ProdutorRest,'/produtor',endpoint='produtores')
api.add_resource(rest.ApoliceRest,'/apolice',endpoint='apolices')
api.add_resource(rest.SeguradoRest,'/segurado',endpoint='segurados')

pdf_handler=PDFHandler()
@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    filename = request.args.get('filename')  # Obtém o nome do arquivo da consulta (query parameter)
    return pdf_handler.download_pdf(filename)
'''
def download_pdf():
    filename = request.args.get('filename')  # Obtém o nome do arquivo da consulta (query parameter)

    # Verifique se o arquivo PDF solicitado existe no diretório
    pdf_directory = 'C:\\Users\\pedro\\Documents\\Site\\Apolice_Seguros_2023\\'
    pdf_path = os.path.join(pdf_directory, filename+".pdf")

    print(pdf_path)

    if os.path.exists(pdf_path) and pdf_path.endswith('.pdf'):
        # Envie o arquivo PDF como resposta
        return send_file(pdf_path, as_attachment=True)
    else:
        return 'Arquivo PDF não encontrado', 404  # Resposta de erro caso o arquivo não seja encontrado

'''

if __name__=="__main__":
    app.run(debug=True)
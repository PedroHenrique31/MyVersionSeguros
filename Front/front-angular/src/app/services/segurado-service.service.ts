import { Injectable } from '@angular/core';
import {Observable } from 'rxjs';
import { HttpClient } from  '@angular/common/http';
import { Segurado } from '../segurado/segurado';
import { SeguradoDetalhes, Telefone } from '../segurado-detail/segurado-detail';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SeguradoService {
  private url='/api/segurado';

  constructor(private _http:HttpClient) { }

    // Realiza um GET para API e pega a lista de todos os segurados em JSON.
    getAll():Observable<Segurado[]>{
      return this._http.get<Segurado[]>(this.url).pipe(map(//mapeia os valores do array de any, para Segurado.
        (dado:any[])=>{
          return dado.map(
          item => ({//atribui um valor para cada objeto typescript como um valor do JSON
          COD:item.COD,
          NOME:item.NOME,
          CPF:item.CPF,
          RG:item.RG,
          profissao:item.PROFISSAO,
          empresa:item.EMPRESA,
          renda:parseFloat(item.RENDA),
          dataNascimento:new Date(item.DATA_NASCIMENTO),
          Obs:item.OBSERVACAO
        }))} ));
   }// Fim getAll

   getByName(nome:string):Observable<Segurado[]>{
    
    let urlFinal=this.url+"?NOME="+nome;
    return this._http.get<Segurado[]>(urlFinal).pipe(map(//mapeia os valores do array de any, para Segurado.
    (dado:any[])=>{
      return dado.map(
      item => ({//atribui um valor para cada objeto typescript como um valor do JSON
      COD:item.COD,
      NOME:item.NOME,
      CPF:item.CPF,
      RG:item.RG,
      profissao:item.PROFISSAO,
      empresa:item.EMPRESA,
      renda:parseFloat(item.RENDA),
      dataNascimento:new Date(item.DATA_NASCIMENTO),
      Obs:item.OBSERVACAO
    }))} ));
   }

  getOne(cod: number): Observable<SeguradoDetalhes> {
    console.log("Chamou a função getOne");
    let urlFinal = this.url + "?COD=" + cod;
    return this._http.get<any>(urlFinal).pipe(
      map(data => {
        const seguradoDetalhes: SeguradoDetalhes = new SeguradoDetalhes();
        seguradoDetalhes.COD = data.COD;
        seguradoDetalhes.NOME = data.NOME;
        seguradoDetalhes.CPF = data.CPF;
        seguradoDetalhes.RG = data.RG;
        seguradoDetalhes.profissao = data.PROFISSAO;
        seguradoDetalhes.empresa = data.EMPRESA;
        seguradoDetalhes.renda = data.RENDA;
        seguradoDetalhes.dataNascimento = data.DATA_NASCIMENTO ? new Date(data.DATA_NASCIMENTO) : new Date('1901-01-01');
        seguradoDetalhes.Obs = data.OBSERVACAO;

        // Mapear Telefones
        if (data.TELEFONES) {
          console.log("entrou nesse if telefones em getOne");
          seguradoDetalhes.telefones = data.TELEFONES.map((tel:any) => ({
            DDD: tel.DDD,
            telefone: tel.FONE
          }));
        }

        // Mapear Emails
        if (data.EMAILS) {
          console.log("entrou nesse if emails em getOne");
          seguradoDetalhes.emails = data.EMAILS.map((email:any) => ({
            cod: email.COD,
            email: email.EMAIL
          }));
        }

        // Mapear Endereços
        if (data.ENDERECOS) {
          console.log("entrou nesse if enderecos em getOne");
          seguradoDetalhes.enderecos = data.ENDERECOS.map((endereco:any) => ({
            cod: endereco.COD,
            endereco: endereco.ENDERECO,
            tipo: endereco.TIPO,
            bairro: endereco.BAIRRO,
            cidade: endereco.CIDADE,
            uf: endereco.UF,
            cep: endereco.CEP
          }));
        }

        //Mapear apolices
        if(data.APOLICES){
          console.log("entrou nesse if apolices em getOne");
          seguradoDetalhes.apolices = data.APOLICES.map(
            (apolice:any) =>({
              cod:apolice.COD,
              premioLiquido:apolice.PREMIO_LIQUIDO,
              ramo:apolice.RAMO,
              seguradora:apolice.SEGURADORA
            }));
        }

        console.log("telefones em getOne: "+seguradoDetalhes.telefones.length);
        console.log("enderecos em getOne: "+seguradoDetalhes.enderecos.length);
        console.log("emails em getOne: "+seguradoDetalhes.emails.length);
        
        //TODO: Fazer algo aqui para só retornar resultado quando tiver os dados todos preenchidos.
        return seguradoDetalhes;
      })
    ); //Fim get
  }//Fim getOne()

}//Fim classe.

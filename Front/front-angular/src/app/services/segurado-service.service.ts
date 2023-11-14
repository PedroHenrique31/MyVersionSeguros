import { Injectable } from '@angular/core';
import {Observable } from 'rxjs';
import { HttpClient } from  '@angular/common/http';
import { Segurado } from '../segurado/segurado';
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

   getOne(cod:number):Observable<Segurado>{
    let urlFinal=this.url+"?COD="+cod;
    return this._http.get<Segurado>(urlFinal);

    //Acessa o banco e retorna um segurado;
   }
}//Fim classe.

import { Injectable } from '@angular/core';
import { Apolice, ApoliceDetalhada } from '../apolice/apolice';
import {Observable, Subscriber } from 'rxjs';
import { HttpClient } from  '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ApoliceService {
  private url='/api/apolice';
  
  

  constructor(private _http:HttpClient) { }

  //Realiza um GET para API e pega uma apolice especifica.
  //TODO:DESCOBRIR COMO ISSO FUNCIONA E pegar uma apolice por vez
  getOne(codigo: number): Observable<ApoliceDetalhada> {
    let url_Final = this.url + "?COD=" + codigo;
    console.log("Url_final: " + url_Final);
  
    return this._http.get<ApoliceDetalhada>(url_Final).pipe(
      map((data: any) => ({
        COD: data.COD,
        inivigor: new Date(data.INIVIGOR),
        fimvigor: new Date(data.FIMVIGOR),
        linkApolice: data.LINK_APOLICE,
        produto: data.PRODUTO,
        ramo: data.RAMO,
        seguradora: data.SEGURADORA,
        premioLiquido: parseFloat(data.premio_liquido),
        premioTotal: parseFloat(data.premio_total),
        cod_segurado: data.COD_SEGURADO,
        cod_produtor: data.COD_PRODUTOR,
        nomeProdutor:data.PRODUTOR_NOME,
        nomeSegurado:data.SEGURADO_NOME
      }))
    );
  }
  //TODO: Essa função conecta com a API para buscar uma lista igual getAll, retorna Observable
  getByMes(mes:number):Observable<Apolice[]>{
    let url_Final=this.url+"?MESVENCIMENTO="+mes;
    return this._http.get<any[]>(url_Final).pipe(
      map((data:any[]) =>{
        return data.map(item =>({
          COD:item.COD,
          inivigor:new Date(item.INIVIGOR),
          fimvigor: new Date(item.FIMVIGOR),
          linkApolice:item.LINK_APOLICE,
          produto:item.PRODUTO,
          ramo:item.RAMO,
          seguradora:item.SEGURADORA,
          premioLiquido:parseFloat(item.premio_liquido),
          premioTotal:parseFloat(item.premio_total),
          cod_segurado:item.COD_SEGURADO,
          cod_produtor:item.COD_PRODUTOR
        }));

      }
      ));
  }

  // Realiza um GET para API e pega a lista de todos as apolices em JSON.
  getAll(): Observable<Apolice[]> {
    return this._http.get<any[]>(this.url).pipe(
      map((data: any[]) => {
        return data.map(item => ({
          COD: item.COD,
          inivigor: new Date(item.INIVIGOR),
          fimvigor: new Date(item.FIMVIGOR),
          linkApolice: item.LINK_APOLICE,
          produto: item.PRODUTO,
          ramo: item.RAMO,
          seguradora: item.SEGURADORA,
          premioLiquido: parseFloat(item.premio_liquido),
          premioTotal: parseFloat(item.premio_total),
          cod_segurado:item.COD_SEGURADO,
          cod_produtor:item.COD_PRODUTOR

        }));
      })
    );
  }

  getArquivo():Observable<Blob>{
    let url_download="/api/download_apolice";
    // Faz a solicitação GET para a URL do arquivo PDF
    return this._http.get(url_download, { responseType: 'blob'});
  }
}

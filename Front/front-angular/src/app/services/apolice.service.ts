import { Injectable } from '@angular/core';
import { Apolice } from '../apolice/apolice';
import {Observable } from 'rxjs';
import { HttpClient } from  '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ApoliceService {
  private url='/api/apolice';
  
  

  constructor(private _http:HttpClient) { }

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

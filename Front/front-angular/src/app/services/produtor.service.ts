import { Injectable } from '@angular/core';
import { Produtor } from '../produtor/produtor';
import {Observable } from 'rxjs';
import { HttpClient } from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProdutorService {
  private url='/api/produtor';

  constructor(private _http:HttpClient) {

   }

   // Realiza um GET para API e pega a lista de todos os produtores em JSON.
   getAll():Observable<Produtor[]>{
      return this._http.get<Produtor[]>(this.url);
   }


}

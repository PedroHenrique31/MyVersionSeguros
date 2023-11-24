import { Component } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Segurado } from '../segurado/segurado';
import { SeguradoDetalhes } from './segurado-detail';
import { SeguradoService } from '../services/segurado-service.service';

@Component({
  selector: 'app-segurado-detail',
  templateUrl: './segurado-detail.component.html',
  styleUrls: ['./segurado-detail.component.css']
})
export class SeguradoDetailComponent {

  segurado?:SeguradoDetalhes;
  constructor(private seguradoService:SeguradoService,private rota: ActivatedRoute){
    this.getSegurado();
  }
  getSegurado(){
    
    let codigo=this.rota.snapshot.paramMap.get("COD");
    let cod=Number(codigo);
    //TODO: falta criar um método no service para enviar solicitações ao banco.
    this.seguradoService.getOne(cod).subscribe((x) =>{this.segurado=x;
      
    });
   
  }//fimGetSegurado


}

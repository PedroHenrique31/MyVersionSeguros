import { Component } from '@angular/core';
import { Segurado } from './segurado';
import { SeguradoService } from '../services/segurado-service.service';

@Component({
  selector: 'app-segurado',
  templateUrl: './segurado.component.html',
  styleUrls: ['./segurado.component.css']
})
export class SeguradoComponent {
  segurados:Segurado[]=[];

  constructor(private seguradoAPI:SeguradoService){
    this.getSeguradosTodos();
  }
  getSeguradosTodos():void{
    this.seguradoAPI.getAll().subscribe(
      (x)=>(this.segurados=x));
  }


}

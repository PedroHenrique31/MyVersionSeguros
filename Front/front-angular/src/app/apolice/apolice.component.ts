import { Component } from '@angular/core';
import { Apolice } from './apolice';
import { ApoliceService } from '../services/apolice.service';

@Component({
  selector: 'app-apolice',
  templateUrl: './apolice.component.html',
  styleUrls: ['./apolice.component.css']
})
export class ApoliceComponent {
  //Lista de objetos do tipo Apolice vazia pois vem do BD.
  apolices:Apolice[]=[];
  apoliceSelecionada=false;

  constructor(private apoliceAPI:ApoliceService){
    this.getTodasApolices();
    console.log("Tamanho de apolices: "+this.apolices.length);
  }

  getTodasApolices():void{
    this.apoliceAPI.getAll().subscribe((apolice)=>(this.apolices=apolice));
    
  }


}

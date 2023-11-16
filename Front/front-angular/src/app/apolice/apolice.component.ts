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
  //apoliceEspecifica:Apolice;
  apoliceSelecionada=false;
  dataHoje:Date=new Date(2023,11,16);
  mes=11;

  constructor(private apoliceAPI:ApoliceService){
    this.dataHoje=new Date();
    this.mes=this.dataHoje.getMonth()+1;
    this.getApolicesMes(this.mes);
    
    
  }

  getTodasApolices():void{
    this.apoliceAPI.getAll().subscribe((apolice)=>(this.apolices=apolice));
    
  }
  getApolicesMes(mes:number):void{
    this.apoliceAPI.getByMes(mes).subscribe((apolice) => (
      this.apolices=apolice
    ));
  }
  getApoliceEspecifica(cod:number){
    let apolice=this.apoliceAPI.getOne(cod);
    console.log(apolice);
  }

}

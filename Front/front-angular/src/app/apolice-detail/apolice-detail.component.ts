import { Component } from '@angular/core';


import { ActivatedRoute } from '@angular/router';
import { ApoliceService } from '../services/apolice.service';
import { Apolice, ApoliceDetalhada } from '../apolice/apolice';


@Component({
  selector: 'app-apolice-detail',
  templateUrl: './apolice-detail.component.html',
  styleUrls: ['./apolice-detail.component.css']
})
export class ApoliceDetailComponent {

  apolice?:ApoliceDetalhada
  urlGeral='http://localhost:4200/api/download_apolice?filename=';
  urlApolice="";

  constructor(private apoliceService:ApoliceService,private rota:ActivatedRoute){
    this.getApolice();
    //this.geraLink();
  }

  getApolice(){
    let codigo=this.rota.snapshot.paramMap.get("COD"),
    cod=Number(codigo);
    this.apoliceService.getOne(cod).subscribe((x) =>(this.apolice=x));
    this.geraLink();
  }
  geraLink():string{
    if(this.apolice){
      return this.urlGeral+this.apolice.linkApolice;
    }else{
      console.log("Não gerou o link");
      return '';
    }
  }
}

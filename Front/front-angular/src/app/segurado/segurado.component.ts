import { Component } from '@angular/core';
import { Segurado } from '../segurado/segurado';
import { SeguradoService } from '../services/segurado-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-segurado',
  templateUrl: './segurado.component.html',
  styleUrls: ['./segurado.component.css']
})
export class SeguradoComponent {
  segurados:Segurado[]=[];
  nomePesquisa:string='';
  feitaPesquisa:boolean=false;

  constructor(private seguradoAPI:SeguradoService,private roteador:Router){
    this.getSeguradosTodos();
  }
  getSeguradosTodos():void{
    this.seguradoAPI.getAll().subscribe(
      (x)=>(this.segurados=x));
  }

  pesquisaSeguradoPorNome(){
    //console.log("chamou pesquisaSeguradoPorNome");
    this.seguradoAPI.getByName(this.nomePesquisa).subscribe((a)=>(this.segurados=a));
    this.feitaPesquisa=true;
  }
 navegarParaNovoSegurado():void{
    this.roteador.navigate(['segurado/novo/novo_segurado']);
 }

}

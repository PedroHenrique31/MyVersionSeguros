import { Component } from '@angular/core';
import { ProdutorService } from '../services/produtor.service';
import { Produtor } from './produtor';

@Component({
  selector: 'app-produtor',
  templateUrl: './produtor.component.html',
  styleUrls: ['./produtor.component.css']
})


export class ProdutorComponent { 
  //Lista de objetos do tipo Produtor vazia pois vem do BD.
  funcionarios:Produtor[]=[];
  
  // construtor que adiciona objeto da classe ProdutorComponent como private.
  constructor(private produtorAPI:ProdutorService){
    this.getProdutor();
  }
  // não sei pra que serve.
  ngOnInit():void{}

  /* metodos get que retorna void não sei pq, 
  mas ele é o elemento de maior abstração que usa o service pra pegar dados do banco */
  getProdutor():void {
      this.produtorAPI.getAll().subscribe((x)=>(this.funcionarios=x));
  }

}

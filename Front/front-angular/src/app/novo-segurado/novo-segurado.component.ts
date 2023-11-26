import { Component } from '@angular/core';
import { SeguradoDetalhes } from '../segurado-detail/segurado-detail';
import { Segurado } from '../segurado/segurado';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-novo-segurado',
  templateUrl: './novo-segurado.component.html',
  styleUrls: ['./novo-segurado.component.css']
})
export class NovoSeguradoComponent {
  novoSegurado:SeguradoDetalhes=new SeguradoDetalhes();
  seguradoSimples?:Segurado;
  etapa:number=0;
  formulario:FormGroup;

  /*Criamos um objeto formulario que contém os campos do nosso formulário, com isso 
  podemos implementar regras de negócio e validações nos campos do form de forma reativa.
  */
 
  constructor(private formBuilder:FormBuilder){
    this.formulario=this.formBuilder.group({
      nome: ['', Validators.required],
      dataNascimento: [new Date(), Validators.required],
      cpf: ['', Validators.required],
      rg: ['', Validators.required],
      profissao: [''],
      empresa: [''],
      renda: [0, Validators.min(0)],
      observacao: [''],
    });
    console.log("etapa: "+this.etapa);
  }

 
  vaiProximaEtapa():void{
    this.etapa++;
    this.submitFormulario();
  }

  /* Ao fazermos o submit podemos acessar os elementos do formulario e atribuir ao objeto
  e aí sim enviar o objeto para o banco
  */
 
  submitFormulario(){
    this.novoSegurado.NOME=this.formulario.get('nome')?.value;
    this.novoSegurado.CPF=this.formulario.get('cpf')?.value;
    this.novoSegurado.RG=this.formulario.get('rg')?.value;
    this.novoSegurado.dataNascimento=this.formulario.get('dataNascimento')?.value;

    console.log(JSON.stringify(this.novoSegurado, null, 2));

  }
  

}

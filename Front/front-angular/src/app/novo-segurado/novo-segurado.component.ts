import { Component } from '@angular/core';
import * as TodasClasses from '../segurado-detail/segurado-detail';
import  {Segurado} from '../segurado/segurado';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-novo-segurado',
  templateUrl: './novo-segurado.component.html',
  styleUrls: ['./novo-segurado.component.css']
})
export class NovoSeguradoComponent {
  novoSegurado:TodasClasses.SeguradoDetalhes=new TodasClasses.SeguradoDetalhes();
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
      observacao: ['',Validators.maxLength(45)],
      telefone:[''],
      DDD:[''],
      email:['',Validators.email],
      enderecoCompleto:[''],
      tipoEndereco:[''],
      bairro:[''],
      cidade:[''],
      uf:[''],
      cep:[''],
    });
    console.log("etapa: "+this.etapa);
    
  }

 
  vaiProximaEtapa():void{
    this.etapa++;
    this.submitFormulario();
  }
  adicionaTelefone(){
    let DDD='61',tel='1234567';
    let telefoneNovo:TodasClasses.Telefone;

    telefoneNovo={DDD:'ab',telefone:'ab',COD:0};
    telefoneNovo.DDD=DDD;
    telefoneNovo.telefone=tel;
    this.novoSegurado.telefones.push(telefoneNovo);
    //TODO:Adicionar uma visualização no front
    console.log(JSON.stringify(this.novoSegurado, null, 2));

  }
  adicionaEmail(){
    let emailNovoTexto='emailPadraoCodigo';
    let emailNovo:TodasClasses.Email={cod:0,email:'emailVazio'};
    emailNovo.email=emailNovoTexto;
    this.novoSegurado.emails.push(emailNovo);
    //TODO:Adicionar uma visualização no front
    console.log(JSON.stringify(this.novoSegurado, null, 2));

  }
  adicionaEndereco(){
    let enderecoTexto='endereco padrão pra preencher essa firula',
    tipoEnd='firula2',
    bairroEnd='firula3',
    cidadeEnd='firula4',
    ufEnd='firula5',
    cepEnd='firula6';
    let enderecoNovo:TodasClasses.Endereco={cod:0,endereco:'firula1',tipo:'firula2',bairro:'firula3',
    cidade:'firula4',uf:'fi',cep:'firula5'};
    
    //TODO: Adicionar todo o resto dos campos
    enderecoNovo.endereco=enderecoTexto;
    enderecoNovo.tipo=tipoEnd;
    enderecoNovo.bairro=bairroEnd;
    enderecoNovo.cidade=cidadeEnd;
    enderecoNovo.uf=ufEnd;
    enderecoNovo.cep=cepEnd;

    //TODO:Adicionar uma visualização no front
    this.novoSegurado.enderecos.push(enderecoNovo);
    console.log(JSON.stringify(this.novoSegurado, null, 2));

  }

  /* Ao fazermos o submit podemos acessar os elementos do formulario e atribuir ao objeto
  e aí sim enviar o objeto para o banco
  */
 
  submitFormulario(){
    this.novoSegurado.NOME=this.formulario.get('nome')?.value;
    this.novoSegurado.CPF=this.formulario.get('cpf')?.value;
    this.novoSegurado.RG=this.formulario.get('rg')?.value;
    this.novoSegurado.dataNascimento=this.formulario.get('dataNascimento')?.value;
    
    //De alguma forma preciso ver como salvar etapas do novoSegurado, pois isso será útil no futuro.

    console.log(JSON.stringify(this.novoSegurado, null, 2));

  }
  

}

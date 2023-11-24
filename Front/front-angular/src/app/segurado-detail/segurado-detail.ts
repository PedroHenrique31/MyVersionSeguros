import { Segurado } from "../segurado/segurado";

export interface Telefone{
    DDD:string,
    telefone:string
}
export interface Email{
    cod:number,
    email:string
}
export interface Endereco{
    cod:number,
    endereco:string,
    tipo:string,
    bairro:string,
    cidade:string,
    uf:string,
    cep:string
}
export interface ApoliceSegurado{
    COD:number,
    premioLiquido:number,
    ramo:string,
    seguradora:string
}

export class SeguradoDetalhes implements Segurado {
    telefones:Telefone[]=[];
    emails:Email[]=[];
    enderecos:Endereco[]=[];
    COD: number=0;
    NOME:string='';
    CPF:string='';
    RG:string='';
    profissao:string='';
    empresa:string='';
    renda:number=0;
    dataNascimento:Date=new Date('2023-01-03');
    Obs:string='';
    apolices:ApoliceSegurado[]=[];


}
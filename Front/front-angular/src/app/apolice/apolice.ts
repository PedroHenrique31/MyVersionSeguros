export interface Apolice{
    COD:number,
    inivigor:Date,
    fimvigor:Date,
    linkApolice:string,
    produto:string,
    ramo:string,
    seguradora:string,
    premioLiquido:number,
    premioTotal:number,
    cod_segurado:number,
    cod_produtor:number
} 
export interface ApoliceDetalhada extends Apolice{
    nomeProdutor:string,
    nomeSegurado:string
}
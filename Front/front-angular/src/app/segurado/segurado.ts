// Define a estrutura de dado do segurado que será preenchida com o que vem do banco
export interface Segurado{
    COD: number,
    NOME:string,
    CPF:string,
    RG:string,
    profissao:string,
    empresa:string,
    renda:number,
    dataNascimento:Date,
    Obs:string
}
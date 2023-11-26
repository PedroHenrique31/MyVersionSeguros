# MyVersionSeguros
Projeto do sistema de informação de uma corretora de seguros que decidi montar.
Nele vou criar um sistema de informação para uma corretor de seguros genérica, mas estou
me baseando num modelo que já havia começado antes, portanto já possuo uma base de dados
que não será mostrada aqui, porém sua estrutura e seu diagrama entidade relacionamento
está colocado em pdf aqui.

# Coisas que estão faltando:

4. Idealizar funções de dashboard, levantar quais requisitos irei mostrar no dashboard;
- 4.1.  Verificar quais funções de pesquisa do dashboard precisam de uma função correspondente na API(receita total é um caso). 
5. Implementar todas as demais funções de REST, com os verbos DELETE.
6. Adicionar estilos com CSS.
7. Amanhã adicionarei a rota para pagina de criação de segurado e trabalharei nela;

## Algumas decisões que tomei
Decidi por uma questão de tempo e praticidade não trabalhar
as funções PUT e POST para o caso onde o usuário quer alterar **APENAS**
dados nas tabelas filhas como TELEFONE,ENDERECO e EMAIL, até porquê 
não tenho interesse em realizar isso agora, pois poderia numa próxima atualização
fazer a relação entre esses entes ser N:N, assim o usuário poderia inserir outros contatos
indiretos a pessoa, como o número de outro segurado que se saber ser pai/mãe deste.
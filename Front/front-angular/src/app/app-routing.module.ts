/* Arquivo criado diretamente no diretório com esse nome, aqui 
importamos os components e definimos rotas para ele que o angular usará pra criar cdigo 
javascript que leava a essas paginas.*/
import { NgModule } from "@angular/core";
import { Routes,RouterModule } from "@angular/router";

import { AppComponent } from "./app.component";
import { ProdutorComponent } from "./produtor/produtor.component";
import { SeguradoComponent } from "./segurado/segurado.component";
import { ApoliceComponent } from "./apolice/apolice.component";
import { ApoliceDetailComponent } from "./apolice-detail/apolice-detail.component";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { SeguradoDetailComponent } from './segurado-detail/segurado-detail.component';

const routes: Routes=[
    {path:'',component:AppComponent},
    {path:'dash',component:DashboardComponent},
    {path:'produtor', component:ProdutorComponent},
    {path:'segurado',component:SeguradoComponent},
    {path:'apolices',component:ApoliceComponent},
    {path:'apolices/:COD',component:ApoliceDetailComponent},
    {path:'segurado/:COD',component:SeguradoDetailComponent}
    //{ path: 'visualizar-pdf', component: VisualizarPdfComponent }
];

@NgModule({
    declarations:[],
    imports:[RouterModule.forRoot(routes)],
    exports:[RouterModule]
})

export class AppRoutingModule{}
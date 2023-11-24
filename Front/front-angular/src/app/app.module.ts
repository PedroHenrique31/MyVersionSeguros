import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import {MatButtonModule} from '@angular/material/button';
import { MatCommonModule } from '@angular/material/core';
import { ActivatedRoute } from '@angular/router';

// import dos componentes que serão usados na aplicação em geral
import { AppComponent } from './app.component';
import { ProdutorComponent } from './produtor/produtor.component';
import { AppRoutingModule } from './app-routing.module';
import { ApoliceComponent } from './apolice/apolice.component';
import { SeguradoComponent } from './segurado/segurado.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ApoliceDetailComponent } from './apolice-detail/apolice-detail.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SeguradoDetailComponent } from './segurado-detail/segurado-detail.component';
import { NovoSeguradoComponent } from './novo-segurado/novo-segurado.component';
//import { PDFViewerModule } from 'ngx-extended-pdf-viewer';
//import { VisualizarPdfComponent } from './visualizar-pdf-component/visualizar-pdf-component.component';

@NgModule({
  declarations: [
    AppComponent,
    ProdutorComponent,
    ApoliceComponent,
    SeguradoComponent,
    ApoliceDetailComponent,
    DashboardComponent,
    SeguradoDetailComponent,
    NovoSeguradoComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    FormsModule,
    MatTableModule,
    MatCommonModule,
    MatButtonModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

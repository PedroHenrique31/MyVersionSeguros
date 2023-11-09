import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import { MatCommonModule } from '@angular/material/core';

// import dos componentes que serão usados na aplicação em geral
import { AppComponent } from './app.component';
import { ProdutorComponent } from './produtor/produtor.component';
import { AppRoutingModule } from './app-routing.module';
import { ApoliceComponent } from './apolice/apolice.component';
import { SeguradoComponent } from './segurado/segurado.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
//import { PDFViewerModule } from 'ngx-extended-pdf-viewer';
//import { VisualizarPdfComponent } from './visualizar-pdf-component/visualizar-pdf-component.component';

@NgModule({
  declarations: [
    AppComponent,
    ProdutorComponent,
    ApoliceComponent,
    SeguradoComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    FormsModule,
    MatTableModule,
    MatCommonModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

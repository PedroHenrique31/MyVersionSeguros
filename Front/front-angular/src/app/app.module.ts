/* Nesse arquivo nós importamos os codigos que vamso usar nesse módulo. */
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FormsModule} from '@angular/forms';
import { MatTableModule } from '@angular/material/table';

//import { ProdutorComponent } from './produtor.component';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    MatTableModule
    //ProdutorComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

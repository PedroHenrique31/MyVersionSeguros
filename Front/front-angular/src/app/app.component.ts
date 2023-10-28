import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  numero : number = 1;


  aumentar(){
    this.numero ++;
  }


  diminuir(){
    this.numero --;
  }


  repete(n: number): Array<number> {
    return Array(n);
  }


}

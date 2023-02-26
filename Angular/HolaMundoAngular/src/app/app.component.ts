import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'HolaMundo';
  usuario= 'Carlos';


  recibirMensajeDelHijo(evento: string){
    alert(evento)
  }
}

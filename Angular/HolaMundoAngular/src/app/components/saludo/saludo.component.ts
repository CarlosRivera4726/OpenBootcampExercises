import { Component, Input, Output, EventEmitter, OnInit, OnDestroy, OnChanges, SimpleChanges} from '@angular/core';

@Component({
  selector: 'app-saludo',
  templateUrl: './saludo.component.html',
  styleUrls: ['./saludo.component.scss']
})
export class SaludoComponent implements OnInit, OnDestroy, OnChanges{

  @Input() nombre: string = "Anónimo";
  @Output() mensaje: EventEmitter<string> = new EventEmitter<string>();

  constructor(){

  }

  ngOnInit(): void {
    console.log("ngOnInit del componente saludo")
  }


  ngOnChanges(changes: SimpleChanges): void {
    
    console.log("ngChanges Cambios")
  }
  ngOnDestroy(): void {

    console.log("ngDestroy El componente se va a destruir")
  }

  /* Ejemplo para gestionar un evento click*/
  //alertaSaludo(): void{
  //  alert(`Hola ${this.nombre}. Alerta despachada`)
  //}
  /*Ejemplo para gestionar un evento de tipo click en el DOM y enviar un texto al componente padre */
  enviarMensajeAlPadre(): void{
    this.mensaje.emit(`Hola, ${this.nombre}. Alerta despachada`);
  }
}

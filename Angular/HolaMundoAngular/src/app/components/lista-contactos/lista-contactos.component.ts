import { Component, OnDestroy, OnInit } from '@angular/core';
import { IContacto } from 'src/app/models/contacto.interface';
import { ContactoService } from 'src/app/services/contacto.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-lista-contactos',
  templateUrl: './lista-contactos.component.html',
  styleUrls: ['./lista-contactos.component.scss']
})
export class ListaContactosComponent implements OnInit, OnDestroy {

  // Creamos el subscription
  subscription: Subscription | undefined;
  // Creamos la lista contactos
  listaContactos: IContacto[] = [];
  contacto: IContacto | undefined;
  //inyectamos en el constructor el servicio de Contactos
  constructor(private contactoService: ContactoService ) {  }

  ngOnInit(): void {
    //Obtenemos la lista de contactos que nos brinda el servicio
    this.contactoService.obtenerContactos()
    .then((lista: IContacto[]) => this.listaContactos = lista)
    .catch((error) => console.error(`Ha surgido un error ${error}`))
    .finally(() => console.info("Carga finalizada"));
  }

  obtenerContactoId(id: number){
    this.subscription = this.contactoService.obtenerContactoID(id)
    ?.subscribe((contacto: IContacto) => this.contacto = contacto),
    (error: Error) => console.error(error)
  }
  limpiar(){
    this.contacto = undefined;
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }

}

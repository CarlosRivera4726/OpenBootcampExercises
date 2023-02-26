import { Injectable } from '@angular/core';
//importamos la lista de contactos mock
import { CONTACTOS } from '../mocks/contactos.mock';
import { IContacto } from '../models/contacto.interface';

// importamos observables de rxjs
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ContactoService {

  constructor() { }

  //? obtiene todos los contactos//
  obtenerContactos(): Promise<IContacto []> {
    return Promise.resolve(CONTACTOS);
  }

  obtenerContactoID(id: number): Observable<IContacto> | undefined {
    // se busca el contacto dentro de la lista de contactos
    const contacto = CONTACTOS.find((contacto: IContacto) => contacto?.id === id);

    // creamos el observable

    let observable: Observable<IContacto> = new Observable(observer => {
      observer.next(contacto); // Emitir un valor a todo componente suscrito
      observer.complete(); // No emitimos más valores
    })

    if(contacto){
      return observable;
    }
    return undefined;
  }
}

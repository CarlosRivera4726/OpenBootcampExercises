import { Injectable } from '@angular/core';
import { LISTA_CONTACTOS } from '../mocks/contact.mock';
import { IContact } from '../models/contact.interface';

@Injectable({
  providedIn: 'root'
})
export class ContactService {

  listaContactos: IContact[] = LISTA_CONTACTOS;


  constructor() { }

  obtenerContactos(sexo?: string): Promise<IContact[]> {
    if(sexo === 'Masculino' || sexo === 'Femenino'){
      let contactosFiltrados: IContact[] = this.listaContactos.filter(contacto => contacto.sexo == sexo);

      return Promise.resolve(contactosFiltrados);

    } else if(sexo == 'todos'){

      return Promise.resolve(this.listaContactos);

    }else{

      return Promise.reject('Filtro incorrecto');

    }
  } 
}

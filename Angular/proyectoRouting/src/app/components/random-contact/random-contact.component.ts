import { Component, OnInit, Input } from '@angular/core';
import { NavigationExtras} from '@angular/router';
import { LISTA_CONTACTOS } from 'src/app/mocks/contact.mock';
import { IContact } from 'src/app/models/contact.interface';
import { IRandomContact, Results } from 'src/app/models/RandomContact';
import { RandomContactService } from 'src/app/services/random-contact.service';

@Component({
  selector: 'app-random-contact',
  templateUrl: './random-contact.component.html',
  styleUrls: ['./random-contact.component.scss']
})
export class RandomContactComponent implements OnInit {

  constructor() { }

  @Input() randomContact: IRandomContact | undefined;


  ngOnInit(): void {

  }

  agregarAContacto(contact: IRandomContact){
    let contactos: IContact[] = LISTA_CONTACTOS;
    const num = Number(contact.phone);
    let contacto: IContact = {id: Number(contactos.lastIndexOf(LISTA_CONTACTOS[LISTA_CONTACTOS.length - 1])),nombre: contact.name.first, apellido: contact.name.last, email: contact.email, telefono: num, sexo: contact.gender}
    contactos.push(contacto);
  }



}

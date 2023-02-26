import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, NavigationExtras, Router } from '@angular/router';
import { IContact } from 'src/app/models/contact.interface';
import { ContactService } from 'src/app/services/contact.service';

@Component({
  selector: 'app-contactos-page',
  templateUrl: './contactos-page.component.html',
  styleUrls: ['./contactos-page.component.scss']
})
export class ContactosPageComponent implements OnInit {

  

  constructor(private router: Router,  private route: ActivatedRoute, private contactService: ContactService) { }

  filtroSexo: string = 'todos'
  listaContactos: IContact[] = [];

  ngOnInit(): void {

    //Obtenemos los queryparams
    this.route.queryParams.subscribe((params) => {
       console.log(params['sexo']);
       if(params['sexo']){
        this.filtroSexo = params['sexo'];
       }
    });

    console.log("Desde contactos: " + this.filtroSexo)

    //Obtenemos la lista de contactos
    this.contactService.obtenerContactos(this.filtroSexo)
    ?.then((listaContactos) => {this.listaContactos = listaContactos})
    ?.catch((error) => {console.error(`Ha ocurrido un error: ${error}`)})
    .finally(() => {console.info("Peticion 'obtener contactos' finalizada")});
  }

  // Ejemplo de paso de informacion entre componentes a través del ESTADO

  volverAHome(contacto: IContact){
    let navigationExtras: NavigationExtras = {
      state: {
        data: contacto
      }
    };
    this.router.navigate(['/home'], navigationExtras);
  }

  //agregar un nuevo contacto
  



}

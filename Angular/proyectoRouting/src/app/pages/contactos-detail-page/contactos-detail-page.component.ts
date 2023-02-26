import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IContact } from 'src/app/models/contact.interface';

@Component({
  selector: 'app-contactos-detail-page',
  templateUrl: './contactos-detail-page.component.html',
  styleUrls: ['./contactos-detail-page.component.scss']
})
export class ContactosDetailPageComponent implements OnInit {

  id: any | undefined;
  contacto: IContact | undefined;
  filtroPrevio: string = 'todos';

  constructor(private route: ActivatedRoute) { }
  
  ngOnInit(): void {
    // aqui leemos los parametros
    this.route.params.subscribe(
      (params: any) =>{
          if(params.id){
            this.id = params.id;
          }
      }
    )
    // mostrar datos
    if(history.state.data){
      this.contacto = history.state.data;
    }
    if(history.state.filtro){
      this.filtroPrevio = history.state.filtro;
    }
  }

}

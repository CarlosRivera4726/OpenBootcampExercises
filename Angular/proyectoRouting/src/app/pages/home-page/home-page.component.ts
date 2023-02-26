import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, NavigationExtras, Router } from '@angular/router';
import { IContact } from 'src/app/models/contact.interface';


@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  token: string | null = null;
  contacto: IContact | undefined;

  constructor(private router: Router) { }
  
  ngOnInit(): void {
    this.token = sessionStorage.getItem('token');

    
    if(history.state.data){
      console.log(history.state.data);
      this.contacto = history.state.data;
    }
    

  }

  navegarAContactos(): void{
    let navigationExtras: NavigationExtras = {
      queryParams: {
        sexo: 'todos'
      }
    }
    this.router.navigate(['/contacts'], navigationExtras);
  }

}

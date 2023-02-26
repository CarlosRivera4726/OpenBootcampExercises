import { Component, OnInit } from '@angular/core';
import { IContact } from 'src/app/models/contact.interface';
import { IRandomContact, Results } from 'src/app/models/RandomContact';
import { RandomContactService } from 'src/app/services/random-contact.service';

@Component({
  selector: 'app-random-contact-page',
  templateUrl: './random-contact-page.component.html',
  styleUrls: ['./random-contact-page.component.scss']
})
export class RandomContactPageComponent implements OnInit {

  contact: IRandomContact | undefined;

  constructor(private randomContactService: RandomContactService){ }

  ngOnInit(): void {
    this.refrezcarContacto();

  }

  refrezcarContacto(){
      this.randomContactService.obtenerRandomContact().subscribe(
      {
        next: (response: Results)=>{
          this.contact = response.results[0];
          console.table(this.contact.name);
        },
        error: (error) =>{
          console.error(`Error: ${error}`);
        },
        complete: () => {
          console.info("Consulta de random contact compelta")
        }
      }

      );
  }

}

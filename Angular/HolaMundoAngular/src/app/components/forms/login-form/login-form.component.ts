import { Component, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit{

  subscribe: Subscription | undefined;
  x: string = "";

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.subscribe = this.authService.login('eve.holt@reqres.in', 'cityslicka').subscribe(
      (response) => {
        console.log("Respuesta: " + response);
        sessionStorage.setItem('token', response.token);
        this.x = response.token;
      },
      (error) => {
        console.error(`Error ocurrido: ` + error);
      },
      () => {
        console.info("Se ha completado la llamad a la API");
      }
    );
  }

}

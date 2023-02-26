import { Injectable } from '@angular/core';

import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { catchError, Observable, retry, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RandomContactService {
  private URL = 'https://randomuser.me/api';


  constructor(private http: HttpClient) { }

  handleError(error: HttpErrorResponse){
    if(error.status === 0){
      console.error(`Ha ocurrido un error. ${error}`);
    }else{
      console.error(`Error en el backend ${error.status}. El error es: ${error.error}`)
    }


    return throwError(()=> new Error('Error en la peticion de contacto aleatorio'))
  }


  // get a random Contact
  obtenerRandomContact(): Observable<any> {
    return this.http.get(this.URL).pipe(
      retry(2),
      catchError(this.handleError)
      );
  }

  obtenerRandomContacts(n: number){
    const opt: HttpParams = new HttpParams().set("results", n);
    return this.http.get(this.URL, {params: opt}).pipe(
      retry(2),
      catchError(this.handleError)
    );
  }

}

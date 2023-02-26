import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { SaludoComponent } from './components/saludo/saludo.component';
// este es el modulo personalizado
import { ListsModule } from './modules/lists/lists.module';
import { ListaContactosComponent } from './components/lista-contactos/lista-contactos.component';
import { LoginFormComponent } from './components/forms/login-form/login-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormularioComponent } from './components/forms/formulario/formulario.component';
import { FormularioAnidadoComponent } from './components/forms/formulario-anidado/formulario-anidado.component';
import { FormularioArrayComponent } from './components/forms/formulario-array/formulario-array.component';
import { FormularioValidadoComponent } from './components/forms/formulario-validado/formulario-validado.component';

//Importamos de angular material
import { mat } from '../material.module';


@NgModule({
  declarations: [
    AppComponent,
    SaludoComponent,
    ListaContactosComponent,
    LoginFormComponent,
    FormularioComponent,
    FormularioAnidadoComponent,
    FormularioArrayComponent,
    FormularioValidadoComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    // Importamos el modulo personalizado
    ListsModule,
    // Importamos el modulo HttpClientModule para hacer peticiones HTTP
    HttpClientModule,
    BrowserAnimationsModule,
    // Importamos el modulo Reactive FormsModule para trabajar con formularios reactivos
    ReactiveFormsModule,
    //Importamos el modulo material.module.ts <- que tiene todos los modulos
    mat
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ComponenteBasicoComponent } from './componente-basico/componente-basico.component';



@NgModule({
  declarations: [
    ComponenteBasicoComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    // exportamos el componente para que pueda ser utilizado en el resto del proyecto
    ComponenteBasicoComponent
  ]
})
export class ListsModule { }

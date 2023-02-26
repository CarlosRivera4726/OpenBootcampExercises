import { Component, OnInit } from '@angular/core';

import { FormArray, FormGroup, FormBuilder} from '@angular/forms';

@Component({
  selector: 'app-formulario-array',
  templateUrl: './formulario-array.component.html',
  styleUrls: ['./formulario-array.component.scss']
})
export class FormularioArrayComponent implements OnInit {

  miFormularioArray: FormGroup = new FormGroup({});

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.miFormularioArray = this.formBuilder.group({
      nombre: '',
      apellidos: '',
      telefonos: this.formBuilder.array([]) // se inicializa la lista de telefonos vacia
    })
  }

  //Metodo getter para obtener el FormArray de la lista de telefonos
  get telefonoFormulario(): FormArray{
    return this.miFormularioArray.get('telefonos') as FormArray;
  }

  // Método para añadir telefonos a la lista

  anadirTelefono(){
    const telefonoNuevo = this.formBuilder.group({
      prefijo: '',
      numero: ''
    });

    // Añadimos el grupo a la lista de telefonos
    this.telefonoFormulario.push(telefonoNuevo)
  }

  //Método para eliminar un telefono de la lista
  eliminarTelefono(index: number){
    this.telefonoFormulario.removeAt(index);
  }

}

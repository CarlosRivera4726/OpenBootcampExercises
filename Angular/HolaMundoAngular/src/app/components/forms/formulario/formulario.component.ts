import { Component, OnInit } from '@angular/core';

//ejemplo basico de un formulario reactivo
import { FormBuilder, FormGroup } from '@angular/forms';
@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.scss']
})
export class FormularioComponent implements OnInit{

  // definimos nuestro formulario
  miFormulario: FormGroup = new FormGroup({});
  

  // Inyectamos la clase FormBuilder para construir el FormGroup
  constructor(private formBuilder: FormBuilder){ }

  ngOnInit(): void {
    // Iniciamos los campos del formulario y sus valores por defecto
    this.miFormulario = this.formBuilder.group(
      {
        nombre: '',
        apellidos: '',
        email: '',
        telefono: '',
        direccion: ''
      }
    );

    //Nos subscribimos a los cambios que ocurran en el Formulario y los mosytramos por consola
    this.miFormulario.valueChanges.subscribe(
      console.log
    );
  }
}

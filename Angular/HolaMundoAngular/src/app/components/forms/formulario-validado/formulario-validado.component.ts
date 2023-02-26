import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-formulario-validado',
  templateUrl: './formulario-validado.component.html',
  styleUrls: ['./formulario-validado.component.scss']
})
export class FormularioValidadoComponent implements OnInit {

  miFormularioValidado: FormGroup = new FormGroup({});

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {

    this.miFormularioValidado = this.formBuilder.group({
      // campo obligatorio
      nombre: ['', Validators.compose([Validators.required, Validators.pattern('[a-zA-Z]*')])], 
      // Campo no obligatorio
      //apellidos: '',
      apellidos: ['', Validators.compose([Validators.required, Validators.pattern('[a-zA-Z]*')])],

      //Campo obligatorio con valores máximos y minimos
      edad: ['', Validators.compose([Validators.required, Validators.min(18), Validators.max(99)])],
      //Campo obligatorio de tipo email
      email: ['', Validators.compose([Validators.required, Validators.email])],
      //Campo obligatorio de contraseña con regex
      password: ['', Validators.compose([Validators.required, Validators.pattern('[a-zA-Z0-9]*')])],
      // campo booleano con true como obligatorio
      acepta: [false, Validators.requiredTrue]
    })
    
  }

  get nombre(){
    return this.miFormularioValidado.get('nombre');
  }
  get apellidos(){
    return this.miFormularioValidado.get('apellidos');
  }
  get edad(){
    return this.miFormularioValidado.get('edad');
  }
  get email(){
    return this.miFormularioValidado.get('email');
  }
  get password(){
    return this.miFormularioValidado.get('password');
  }
  get acepta(){
    return this.miFormularioValidado.get('acepta');
  }

  //Metodo de submit del formulario
  enviarFormulario(){
    //Controlamos el formulario que sea valido
    if(this.miFormularioValidado.valid){
      console.table(this.miFormularioValidado.value);
      //Reseteamos los campos
      this.miFormularioValidado.reset();
    }
  }

}

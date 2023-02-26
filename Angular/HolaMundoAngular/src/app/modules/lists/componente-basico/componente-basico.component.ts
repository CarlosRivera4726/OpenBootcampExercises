import { Component, OnInit } from '@angular/core';

export type Producto = {
  nombre: string;
  precio: number;
  descripcion: string;
}

@Component({
  selector: 'app-componente-basico',
  templateUrl: './componente-basico.component.html',
  styleUrls: ['./componente-basico.component.scss']
})
export class ComponenteBasicoComponent implements OnInit{

  listaElementos: Producto[] = [
    {
      nombre: 'Leche',
      precio: 10,
      descripcion: "Leche Entera"
    },
    {
      nombre: 'Carne',
      precio: 25,
      descripcion: "Carne de res"
    },
    {
      nombre: 'Huevo',
      precio: 5,
      descripcion: "Huevo AAA"
    }

  ];

  cargando: boolean = false;

  opcion: number = 0;

  constructor(){

  }

  ngOnInit(): void {
    
  }

  cambiarCargando(): void{
    this.cargando = !this.cargando;
  }
  incrementar(): void{
    
    this.opcion++;
  }
}

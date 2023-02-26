/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package objetos;

/**
 *
 * @author Carlos
 */
public class Objetos {

    /*
        Para practicar la encapsulación:

            Crear clase Persona.

            Crear variables las privadas edad, nombre y telefono de la clase Persona.

            Crear gets y sets de cada propiedad.

            Crear un objeto persona en el main.

            Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
        
    */
    public static void main(String[] args) {
        
        Persona persona1 = new Persona();
        String nombre = "Carlos";
        int telefono = 1234;
        int edad = 29;
        persona1.setNombre(nombre);
        persona1.setEdad(edad);
        persona1.setTelefono(telefono);
        
        System.out.println(persona1);
        
    }
    
}

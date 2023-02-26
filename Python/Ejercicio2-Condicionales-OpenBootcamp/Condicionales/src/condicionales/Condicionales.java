package condicionales;

/**
 *
 * @author Carlos
 */
public class Condicionales {

    /*
        En este ejercicio practicarás las estructuras de control, para ello deberás crear:

Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos.

Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:

Incrementar el valor de la variable en uno cada vez que se ejecute.

Mostrarlo por pantalla cada vez que se ejecute.

Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
     */

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int numeroIf = 0;
        if (numeroIf == 0) {
            System.out.println("Numero igual a 0");
        }
        numeroIf = 1;
        if (numeroIf > 0) {
            System.out.println("Numero mayor a 0");
        }
        numeroIf = -1;
        if (numeroIf < 0) {
            System.out.println("Numero menor a 0");
        }
        int numeroWhile = 0;
        while(numeroWhile < 3){
            System.out.println("numeroWhile = " + numeroWhile);
            numeroWhile++;
        }
        do{
            System.out.println("numeroDoWhile = " + numeroWhile);
            numeroWhile++;
        }while(numeroWhile < 3);
        
        for(int numeroFor = 0; numeroFor <=3; numeroFor++ ){
            System.out.println("numeroFor = " + numeroFor);
        }
        int estacion = 1;
        switch(estacion){
            case 1:
                System.out.println("Verano");
                break;
            case 2:
                System.out.println("Invierno");
                break;
            case 3:
                System.out.println("Otoño");
                break;
            case 4:
                System.out.println("Primavera");
                break;
            default:
                System.out.println("Está no es una estacion");
                break;
            
        }
        
    }

}

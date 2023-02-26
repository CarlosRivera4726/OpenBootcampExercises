package ejercicio1;

/**
 *
 * @author Carlos
 */
public class Ejercicio1 {
    // primera parte
    // funcion que sume 3 numeros
    public static void sumarTresNumeros(int num1, int num2, int num3){
        System.out.println(num1 + num2 + num3);
    }

    public static void main(String[] args) {
        sumarTresNumeros(1, 5, 6);
        Coche coche = new Coche();
        System.out.println(coche.numPuertas);
        coche.incrementarPuertas();
        System.out.println(coche.numPuertas);
        
    }
    
}

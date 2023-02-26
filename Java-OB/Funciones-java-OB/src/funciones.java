public class funciones {

    public static void main(String[] args) {
        System.out.println(precioConIva(1000f));
        System.out.println(precioConIva(2000f));
        System.out.println(precioConIva(3000f));
        System.out.println(precioConIva(4000f));
    }


    // funcion que recibe un precio y lo devuelve con el 15% del iva
    private static float precioConIva(float precio){
        float iva = 15f;
        float total = ((iva/100) * precio);
        return total+precio;
    }
}

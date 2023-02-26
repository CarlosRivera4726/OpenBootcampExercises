package Models;

public class Persona {
    String nombre;
    String apellido;
    double numeroTelefono;
    boolean registrado;
    long salario;
    int identificacion;

    public Persona() {
    }

    public Persona(String nombre, String apellido, double numeroTelefono, boolean registrado, long salario, int identificacion) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numeroTelefono = numeroTelefono;
        this.registrado = registrado;
        this.salario = salario;
        this.identificacion = identificacion;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public double getNumeroTelefono() {
        return numeroTelefono;
    }

    public void setNumeroTelefono(double numeroTelefono) {
        this.numeroTelefono = numeroTelefono;
    }

    public boolean isRegistrado() {
        return registrado;
    }

    public void setRegistrado(boolean registrado) {
        this.registrado = registrado;
    }

    public long getSalario() {
        return salario;
    }

    public void setSalario(long salario) {
        this.salario = salario;
    }

    public int getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(int identificacion) {
        this.identificacion = identificacion;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", numeroTelefono=" + numeroTelefono +
                ", registrado=" + registrado +
                ", salario=" + salario +
                ", identificacion=" + identificacion +
                '}';
    }
}

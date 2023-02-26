edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 18:
    print("Eres menor de edad!")
elif edad != 0 and edad >= 18:
    print("Eres mayor de edad!")
else:
    print("Edad no valida!")


def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

respuesta = "Es primo" if is_prime(int(input("Ingrese un numero: "))) else "No es primo"
print(respuesta)

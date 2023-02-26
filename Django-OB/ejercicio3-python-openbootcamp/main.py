

f = open("file.txt", "w")


texto = "Este texto va en el documento"
f.write(texto)

f.close()

f = open("file.txt", "r")
print(f.read)
f.close()


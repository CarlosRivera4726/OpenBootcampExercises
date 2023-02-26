'''
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de 
tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
'''

import sqlite3
database = "basededatos.db"

def buscarAlumnos(nombre=""):
    try:
        conn = sqlite3.connect(database=database)
        cur = conn.cursor()

        data = cur.execute(f"SELECT * FROM Alumnos a WHERE a.nombre=\"{nombre}\"").fetchall()
        print(data)
    
    except:
        pass
    finally:
        cur.close()
        conn.close()

def insertarDatos():
    try:
        data = [ 
            (1, "Carlos", "Rivera"),
            (2, "Felipe", "Gueche"),
            (3, "Andrea", "Montoya"),
            (4, "Florencio", "Montenegro"),
            (5, "Juan", "Oviedo"),
            (6, "Catalina", "Bonilla"),
            (7, "Ana", "Rivera"),
            (8, "Daniela", "Arias")
        ]

        conn = sqlite3.connect(database=database)
        cur = conn.cursor()
        cur.executemany("INSERT INTO Alumnos VALUES(?,?,?)", data)
        
        
    except:
        print("Ya existen los id de los alumnos")
    finally:
        # Hacemos commit para que los cambios se vean reflejados
        conn.commit()
        cur.close()
        conn.close()

def createTable():
    try:
        conn = sqlite3.connect(database=database)
        cur = conn.cursor()
        # Creamos la tabla
        cur.execute("CREATE TABLE Alumnos(id INTEGER, nombre TEXT, apellido TEXT, CONSTRAINT PK_ALUMNOS PRIMARY KEY (id)) ")
        # verificamos que se haya creado
        res = cur.execute("SELECT name FROM sqlite_master")
        print(res.fetchone())
        ## Output: Alumnos

    except sqlite3.OperationalError:
        print("Ya existe la tabla")
    except:
        print("Un error ha ocurrido, contacte con el programador")
    finally:
        cur.close()
        conn.close()
    

def main():
    createTable()
    insertarDatos()
    buscarAlumnos("Carlos")
    buscarAlumnos("a")
    






if __name__ == '__main__':
    main()

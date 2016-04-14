import sqlite3

def tabla():
    try:
        print("welcome")
        conexion= sqlite3.connect("C:/Users/SQL Server Distributed Replay Client/Desktop/sqlite3/db")
        consulta = conexion.cursor()
        sql = """CREATE TABLE db (
         NOMBRE  CHAR(50) NOT NULL,
         APELLIDO  CHAR(50),
         EDAD INT,
         SEXO CHAR(1) )"""

        if (consulta.execute(sql)):
            print("Tabla creada")

    except Exception:
        print("Error")

        consulta.close()
        conexion.commit()
        conexion.close()

def ingresar_datos ():

    name=input("Nombre")
    apell=input("Apellido")
    year=input("Edad")

    conexion=sqlite3.connect("C:/Users/SQL Server Distributed Replay Client/Desktop/sqlite3/db")
    consulta=conexion.cursor()
    argumentos=(name,apell,year)

    sql="""
    INSERT INTO db (NOMBRE,APELLIDO,EDAD)
    VALUES (?,?,?)
    """
    if(consulta.execute(sql,argumentos)):

        print("Registro con Exito" )
    else :
        print("Error")
    consulta.close()

    conexion.commit()
    conexion.close()

if __name__=="__main__":
    tabla()
    ingresar_datos()
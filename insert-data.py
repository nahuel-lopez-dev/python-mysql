# Configuración de la conexión Python y MySQL
# Importando connector de mysql
import mysql.connector
# Para  agregar caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Crear conexión a la base de datos
conexion=mysql.connector.connect(
    host='localhost',
    user='root', 
    password='',
    port='3306',
    database='nombre_db',
    charset='utf8') 

# Crear el cursor
cursor = conexion.cursor()

############# Insertando los datos ##############
# forma de fecha para mysql: año-mes-dia
insertar_datos_tabla1 = """
INSERT INTO tabla1 (id_tabla1, nombre, fecha, long, lat) 
VALUES 
    (1, 'Fulano', '1900-12-30', 48.512995, 50.258882), 
    (2, 'Sultano', '1900-12-30', 48.512995, 50.756767), 
    (3, 'Mengano', '1900-12-30', 48.512995, 50.329381), 
    (4, 'Montoto', '1900-12-30', 48.512995, 50.687439);    
"""

insertar_datos_tabla2 = """
INSERT INTO tabla2 (id_tabla2, nombre, anio, cantidad, id_tabla1)
VALUES
    (1, 'Fulano', 1900, 39666999, 1),
    (2, 'Fulano', 1900, 39666999, 1),
    (3, 'Sultano', 1900, 39666999, 2),
    (4, 'Sultano', 1900, 39666999, 2),
    (5, 'Mengano', 1900, 39666999, 3),
    (6, 'Mengano', 1900, 39666999, 3),
    (7, 'Montoto', 1900, 39666999, 4),
    (8, 'Montoto', 1900, 39666999, 4);
"""

insertar_datos_tabla3 = """
INSERT INTO tabla3 (id_tabla3, nombre, anio, cantidad, id_tabla2)
VALUES
    (1, 'Fulano', 1900, 15000, 1),
    (2, 'Fulano', 1900, 15000, 2),
    (3, 'Sultano', 1900, 15000, 3),
    (4, 'Sultano', 1900, 15000, 4),
    (5, 'Mengano', 1900, 15000, 5),
    (6, 'Mengano', 1900, 15000, 6),
    (7, 'Montoto', 1900, 15000, 7),
    (8, 'Montoto', 1900, 15000, 8);
"""

insertar_datos_tabla4 = """
INSERT INTO tabla4 (id_tabla4, nombre, anio, cantidad, id_tabla4)
VALUES
    (1, 'Fulano', 1900, 20500, 1),
    (2, 'Fulano', 1900, 20500, 2),
    (3, 'Sultano', 1900, 20500, 3),
    (4, 'Sultano', 1900, 20500, 4),
    (5, 'Mengano', 1900, 20500, 5),
    (6, 'Mengano', 1900, 20500, 6),
    (7, 'Montoto', '1900', 20500, 7),
    (8, 'Montoto', '1900', 20500, 8);
"""

# Ejecutando las querys
cursor.execute(insertar_datos_tabla1)
cursor.execute(insertar_datos_tabla2)
cursor.execute(insertar_datos_tabla3)
cursor.execute(insertar_datos_tabla4)

# Guardando los cambios
conexion.commit()    
# Cerrando el cursor y la conexion
cursor.close()
conexion.close()
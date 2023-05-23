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

############### Creando las tablas ###############
# Guardando cada query en una variable, por buenas prácticas
crear_tabla_tabla1 = """
CREATE TABLE tabla1 (
    id_tabla1 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25),
    fecha DATE,
    long FLOAT,
    lat FLOAT
);
"""

crear_tabla_tabla2 = """
CREATE TABLE tabla2 (
    id_tabla2 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25) NOT NULL,
    anio INT,
    cantidad INT,
    id_tabla1 INT,
    FOREIGN KEY (id_tabla1) REFERENCES tabla1(id_tabla1)
);
"""

crear_tabla_tabla3 = """
CREATE TABLE tabla3  (
    id_tabla3 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25),
    anio INT,
    cantidad INT,
    id_tabla2 INT,
    FOREIGN KEY (id_tabla2) REFERENCES tabla2(id_tabla2)
);
"""

crear_tabla_tabla4 = """
CREATE TABLE tabla4 (
    id_tabla4 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25),
    anio INT,
    cantidad INT,
    id_tabla2 INT,
    FOREIGN KEY (id_tabla2) REFERENCES tabla2(id_tabla2)
);
"""

# Ejecutando las querys
cursor.execute(crear_tabla_tabla1)
cursor.execute(crear_tabla_tabla2)
cursor.execute(crear_tabla_tabla3)
cursor.execute(crear_tabla_tabla4)

# Guardando los cambios
conexion.commit()
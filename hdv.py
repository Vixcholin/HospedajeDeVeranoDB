import sqlite3

conexion = sqlite3.connect('hospedajedeverano.db')
cursor = conexion.cursor()

#tabla de ejemplo
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

# Insertar un registro de ejemplo
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)")

# Guardar (commit) los cambios
conexion.commit()

# Consultar los datos
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conexion.close()
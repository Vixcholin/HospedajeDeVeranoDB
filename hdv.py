import sqlite3

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Mostrar todos los nombres de los clientes")
    print("2. Salir")

def mostrar_nombres_clientes(cursor):
    cursor.execute("SELECT Rut FROM Cliente")
    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
    else:
        print("\nNombres de los clientes:")
        for cliente in clientes:
            print(cliente[0]) 

def main():
    conexion = sqlite3.connect('esquema_reserva.db')
    cursor = conexion.cursor()

    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ")

        if opcion == '1':
            mostrar_nombres_clientes(cursor)
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

    conexion.close()

if __name__ == "__main__":
    main()
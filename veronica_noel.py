import csv
import os

# registrar una nueva propiedad

def registrar_propiedad():
    correlativo = input("Ingrese correlativo: ")
    tipo_propiedad = input("Ingrese tipo de propiedad (1 = Casa, 2 = Departamento): ")
    nro_dormitorios = input("Ingrese número de dormitorios: ")
    nro_banos = input("Ingrese número de baños: ")
    precio = input("Ingrese el precio: ")

# validacion y escritura en el archivo CSV
    
    try:
        with open('REGISTRO_PROPIEDADES_USADAS.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([correlativo, 
                             "Casa" if tipo_propiedad == '1' else "Departamento", 
                             nro_dormitorios, 
                             nro_banos, 
                             precio])
        print("Propiedad registrada correctamente.")
    except IOError:
        print("Error al intentar escribir en el archivo.")

# listar todas las propiedades
        
def listar_propiedades():
    try:
        with open('REGISTRO_PROPIEDADES_USADAS.csv', mode='r') as file:
            reader = csv.reader(file)
            print("{:<15} {:<20} {:<20} {:<15} {:<10}".format("CORRELATIVO", "TIPO-DE-PROPIEDAD", 
                                                              "NRO-DE-DORMITORIOS", "NRO-DE-BAÑOS", "PRECIO"))
            for row in reader:
                print("{:<15} {:<20} {:<20} {:<15} {:<10}".format(row[0], row[1], row[2], row[3], row[4]))
    except IOError:
        print("Error al intentar leer el archivo.")

#  imprimir oferta por tipo de propiedad
        
def imprimir_oferta_por_tipo(tipo):
    tipo_texto = "Casa" if tipo == '2' else "Departamento"
    archivo_salida = f'PROPIEDADES_{tipo_texto.upper()}.csv'

    try:
        with open('REGISTRO_PROPIEDADES_USADAS.csv', mode='r') as file:
            reader = csv.reader(file)
            with open(archivo_salida, mode='w', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(["Correlativo", "tipo-propiedad", "nro-de-dormitorios", "nro-de-baños", "precio"])
                for row in reader:
                    if row[1] == tipo_texto:
                        writer.writerow(row)
        print(f"Archivo {archivo_salida} generado correctamente.")
    except IOError:
        print("Error al intentar leer/escribir el archivo.")

# menu
def menu():
    while True:
        print("\n==== Menú Principal ====")
        print("1. Registrar propiedad")
        print("2. Listar propiedades")
        print("3. Imprimir oferta por tipo de propiedad")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_propiedad()
        elif opcion == '2':
            listar_propiedades()
        elif opcion == '3':
            tipo = input("Seleccione tipo de propiedad (1 = Departamento, 2 = Casa): ")
            imprimir_oferta_por_tipo(tipo)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()


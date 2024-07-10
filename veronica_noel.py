import random
import csv
import statistics

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez","Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []
# generar sueldos
def generar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
# clasificar sueldos
def clasificar_sueldos():
    print("Sueldos menores a $800.000")
    print("Total:", len([s for s in sueldos if s < 800000]))
    print("Nombre empleado\tSueldo")
    for i in range(len(trabajadores)):
        if sueldos[i] < 800000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print("Total:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    print("Nombre empleado\tSueldo")
    for i in range(len(trabajadores)):
        if 800000 <= sueldos[i] <= 2000000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
    
    print("\nSueldos superiores a $2.000.000")
    print("TOTAL:", len([s for s in sueldos if s > 2000000]))
    print("Nombre empleado\tSueldo")
    for i in range(len(trabajadores)):
        if sueldos[i] > 2000000:
            print(f"{trabajadores[i]}\t${sueldos[i]}")
    
    print("\nTOTAL SUELDOS: $", sum(sueldos))
# estadisticas
def ver_estadisticas():
    print("Sueldo más alto:", max(sueldos))
    print("Sueldo más bajo:", min(sueldos))
    print("Promedio de sueldos:", sum(sueldos) / len(sueldos))
    print("Media geométrica:", statistics.geometric_mean(sueldos))
# ver sueldos 
def generar_reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i in range(len(trabajadores)):
            sueldo_base = sueldos[i]
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            writer.writerow([trabajadores[i], sueldo_base, desc_salud, desc_afp, sueldo_liquido])
    
    print("Archivo 'reporte_sueldos.csv' generado correctamente.")

# MENU
if __name__ == "__main__":
    while True:
        print("\n===== MENÚ =====")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            generar_sueldos_aleatorios()
            print("Sueldos generados aleatoriamente.")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte_sueldos()
        elif opcion == '5':
            print("Salida exitosa ¡Que tenga buen día!")
            print("""   Desarrollado por Veronica Noel
                RUT: 25.576.384-9""")
            break
        else:
            print("Opción inválida, seleccione una opción válida por favor.")
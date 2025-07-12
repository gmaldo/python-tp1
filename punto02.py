def crear_conjunto():
    conjunto = set()
    print("=== CREACIÓN DE CONJUNTO ===")
    print("Ingresa elementos para el conjunto (escribe 'fin' para terminar):")
    while True:
        elemento = input("Ingresa un elemento: ").strip()
        if elemento.lower() == 'fin':
            break
        conjunto.add(elemento)
        print(f"Elemento '{elemento}' agregado al conjunto.")
        print(f"Conjunto actual: {conjunto}")
    
    return conjunto


def eliminar_elemento(conjunto):
    print("\n=== ELIMINACIÓN DE ELEMENTOS ===")
    
    while True:
        print(f"\nConjunto actual: {conjunto}")
        
        if not conjunto:
            print("El conjunto está vacío. No hay elementos para eliminar.")
            break
        
        elemento = input("Ingresa el elemento a eliminar (escribe 'fin' para terminar): ").strip()
        
        if elemento.lower() == 'fin':
            break
        
        if elemento in conjunto:
            conjunto.remove(elemento)
            print(f"Elemento '{elemento}' eliminado exitosamente.")
        else:
            print(f"El elemento '{elemento}' no está presente en el conjunto.")


def mostrar_menu():
    print("\n" + "="*50)
    print("           GESTOR DE CONJUNTOS")
    print("="*50)
    print("1. Crear un nuevo conjunto")
    print("2. Eliminar elementos del conjunto")
    print("3. Mostrar conjunto actual")
    print("4. Salir")
    print("="*50)


def main():
    conjunto_actual = set()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == "1":
            conjunto_actual = crear_conjunto()
            print(f"\nConjunto creado exitosamente: {conjunto_actual}")
            
        elif opcion == "2":
            if not conjunto_actual:
                print("No hay un conjunto creado. Primero crea un conjunto (opción 1).")
            else:
                eliminar_elemento(conjunto_actual)
                
        elif opcion == "3":
            if not conjunto_actual:
                print("No hay un conjunto creado.")
            else:
                print(f"Conjunto actual: {conjunto_actual}")
                
        elif opcion == "4":
            print("Chau")
            break
            
        else:
            print("Opción no válida. Por favor, seleccioná una opción del 1 al 4.")

main() 
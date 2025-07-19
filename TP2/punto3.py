def verificacion_de_palindromos(palabra: str) -> bool:
    """
    Función que verifica si una palabra es un palíndromo.

    Args:
        palabra (str): La palabra a verificar.

    Returns:
        bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    # Convertir la palabra a minúsculas
    palabra = palabra.lower()
    
    palabra_invertida = palabra[::-1] # invertir la palabra

    if palabra == palabra_invertida: ##veo si son la misma palabra
        return True
    else:
        return False
    
def main():
    palabra_palindroma = "Neuquen"
    if verificacion_de_palindromos(palabra_palindroma):
        print(f"{palabra_palindroma} es un palíndromo.")
    palabra_no_palindroma = "hola"
    if not verificacion_de_palindromos(palabra_no_palindroma):
        print(f"{palabra_no_palindroma} no es un palíndromo.")

main()
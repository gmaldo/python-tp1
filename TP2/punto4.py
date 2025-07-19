def cantidad_de_palabras_y_caracteres(texto: str) -> dict:
    """Cuenta la cantidad de palabras y caracteres en un texto.

    Args:
        texto (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario con la cantidad de palabras y caracteres.
              La estructura del diccionario es:
              {
                  'cantidad_palabras': int,  # Número total de palabras en el texto
                  'cantidad_caracteres': int # Número total de caracteres en el texto
              }
    """
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    cantidad_caracteres = len(texto)
    return {'cantidad_palabras': cantidad_palabras, 'cantidad_caracteres': cantidad_caracteres}

def main():
    texto = input("Ingrese un texto: ")
    resultado = cantidad_de_palabras_y_caracteres(texto)
    print(f"La cantidad de palabras es: {resultado['cantidad_palabras']}")
    print(f"La cantidad de caracteres es: {resultado['cantidad_caracteres']}")

main()
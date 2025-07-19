def es_primo(n: int) -> bool:
    """Determina si un número es primo.
    
    Un número primo es un número natural mayor que 1 que tiene únicamente dos 
    divisores distintos: él mismo y el 1.
    
    Args:
        n (int): Número entero a evaluar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # solo voy hasta la raiz + 1 por si la raiz da entero entero
        if n % i == 0:
            return False  # si tiene un divisor
    return True


def generar_primos_hasta(n: int) -> list[int]:
    """Genera una lista con todos los números primos hasta un número dado.
    
    Un número primo es un número natural mayor que 1 que tiene únicamente dos 
    divisores distintos: él mismo y el 1. Por ejemplo: 2, 3, 5, 7, 11, 13, etc.
    
    Args:
        n (int): Número entero positivo hasta el cual buscar primos (inclusive)
        
    Returns:
        list[int]: Lista con todos los números primos desde 2 hasta n
        
    Raises:
        ValueError: Si n no es un número entero positivo
        
    Examples:
        >>> generar_primos_hasta(10)
        [2, 3, 5, 7]
        >>> generar_primos_hasta(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n < 1:
        raise ValueError("El número debe ser un entero positivo")
    
    primos = []
    for i in range(2, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def main():
    print("primos hasta 10: ", generar_primos_hasta(10))
    print("primos hasta 20: ", generar_primos_hasta(20))
    print("primos hasta 1000: ", generar_primos_hasta(1000))


main()
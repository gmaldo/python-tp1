from functools import reduce

def stats(lista_de_numeros: list[float]) -> dict[str:float]:
    """
    Calcula estadísticas de una lista de números.
    
    Args:
        lista_de_numeros (list[float]): Lista de números para calcular estadísticas.
    
    Returns:
        dict[str, float]: Diccionario con las siguientes estadísticas:
            - "media": Promedio de los números
            - "mediana": Valor central de los números ordenados
            - "moda": Valor que aparece con mayor frecuencia
    
    Example:
        >>> stats([1, 2, 3, 4, 5])
        {'media': 3.0, 'mediana': 3, 'moda': 1}
        
        >>> stats([1, 2, 2, 3, 4])
        {'media': 2.4, 'mediana': 2, 'moda': 2}
    """
    #media
    suma = reduce(lambda x,y: x+y, lista_de_numeros)
    media = suma / len(lista_de_numeros)
    #mediana
    numeros_ordenados = sorted(lista_de_numeros)
    n = len(numeros_ordenados)
    mediana = 0
    if n % 2 != 0:
        mediana = numeros_ordenados[n // 2]
    else:
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        mediana = (medio1 + medio2) / 2
    #moda
    frecuencias = {}
    for numero in lista_de_numeros:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    #max_frecuencia = 0
    #for frecuencia in frecuencias.values():
    #    if frecuencia > max_frecuencia:
    #        max_frecuencia = frecuencia
    max_frecuencia = max(frecuencias.values())
    moda = 0
    for(numero, frecuencia) in frecuencias.items():
        if frecuencia == max_frecuencia:
            moda = numero
    dict = {
        "media": media,
        "mediana": mediana,
        "moda": moda
    }
    return dict;

print(stats([1, 2, 3, 4, 5])) #{'media': 3.0, 'mediana': 3, 'moda': 1}
print(stats([1, 2, 2, 3, 4])) #{'media': 3.0, 'mediana': 3, 'moda': 1}
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(stats(lista_de_numeros)) #{'media': 5.5, 'mediana': 5.5, 'moda': 10}
lista_de_numeros = [1, 2, 3, 4, 4, 4, 4.1, 5, 1, 10] #{'media': 3.81, 'mediana': 4.0, 'moda': 4}
print(stats(lista_de_numeros))

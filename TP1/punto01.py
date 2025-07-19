def ordenar_lista_numeros(lista_numeros):
    conjunto_numeros = set(lista_numeros)  
    lista_ordenada = sorted(list(conjunto_numeros))
    return lista_ordenada


numeros_ejemplo = [5, 2, 8, 1, 9, 3, 5, 2, 7, 4, 6, 1]
print("Lista original:", numeros_ejemplo)
resultado = ordenar_lista_numeros(numeros_ejemplo)
print("Lista ordenada:", resultado)

def convertir_strings_a_caracteres(lista_strings: list[str]):
    """
    Convierte una lista de strings en una nueva lista con listas de caracteres utilizando map.
    
    Esta función toma una lista de strings y devuelve una nueva lista donde cada string
    se convierte en una lista de sus caracteres individuales.
    Args:
        lista_strings (list[str]): Lista de strings a convertir
        
    Returns:
        list[list[str]]: Lista de listas, donde cada sublista contiene los caracteres de un string
    """
    #le aplico con map la funcion list a la lista de string
    return list(map(list,lista_strings))

print(convertir_strings_a_caracteres(["hola","adios"]))
print(convertir_strings_a_caracteres(["python", "map", "list"]))


    

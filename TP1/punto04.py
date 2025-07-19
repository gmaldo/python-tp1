def eliminar_duplicados(lista):
    return list(set(lista))

cadenas = ["phyton", "java", "c", "c#", "javascript", "go", "java","javascript"]
resultado = eliminar_duplicados(cadenas)
print(resultado)
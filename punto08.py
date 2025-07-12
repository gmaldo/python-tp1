def slicing_function(texto):
    dictionary = {}
    datos = texto.split(" | ")  # separamos los por el separador
    for dato in datos:
        clave, valor = dato.split(":") #de cada dato extraemos la parte derecha e izquieda
        valor = valor.strip()
        if valor.isdigit(): #hay que hacer eso porque en el diccionario edad esta sin ""
            valor = int(valor)
        dictionary[clave.strip()] = valor

    return dictionary

text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta"
print(slicing_function(text)) # {"nombre": " Juan Perez", "edad" : 30, "ciudad": "Salta"}
text2 = "Nombre: Ana García | Edad: 25 | Ciudad: Buenos Aires"
print(slicing_function(text2)) # {"nombre": " Ana Garcia", "edad" : 25, "ciudad": "Buenos Aires"}   
set_uno = {1, 2, 3, 4, 5}
set_dos = {4, 5, 6, 7, 8}

set_diff = set_uno - set_dos
print("en el set 2 faltan: ", set_diff)

set_diff = set_dos - set_uno
print("en el set 1 faltan: ", set_diff)

set_diff = set_uno & set_dos
print("en ambos estan: ", set_diff   )

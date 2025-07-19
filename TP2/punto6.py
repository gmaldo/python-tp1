def actualizar_inventario(inventario: dict[str, int], producto_vendido: list[str]) -> dict[str, int]:
    """
    Actualiza el inventario de una tienda restando los artículos vendidos.
    
    Esta función toma un diccionario que representa el inventario actual de una tienda
    y una lista de productos vendidos, luego actualiza las cantidades disponibles
    restando los productos vendidos del inventario.
    
    Args:
        inventario (dict[str, int]): Diccionario con productos como claves y cantidades como valores
        articulos_vendidos (list[str]): Lista de productos vendidos
        
    Returns:
        dict[str, int]: Inventario actualizado con las cantidades reducidas
        
    Raises:
        ValueError: Si se intenta vender un producto que no existe en el inventario
        ValueError: Si no hay suficiente stock para un producto
        
    Examples:
        >>> inventario = {"manzanas": 50, "naranjas": 30, "peras": 20}
        >>> vendidos = ["manzanas", "manzanas", "naranjas", "peras"]
        >>> actualizar_inventario(inventario, vendidos)
        {'manzanas': 48, 'naranjas': 29, 'peras': 19}
        
        >>> inventario = {"notebook": 5, "mouse": 15, "teclados": 8}
        >>> vendidos = ["notebook", "mouse", "mouse", "teclados"]
        >>> actualizar_inventario(inventario, vendidos)
        {'notebook': 4, 'mouse': 13, 'teclados': 7}
    """
    for producto in producto_vendido:
        if producto in inventario:
            if inventario[producto] > 0:
                inventario[producto] -= 1
            else:
                raise ValueError(f"No hay suficiente stock de {producto}")
        else:
            raise ValueError(f"{producto} no existe en el inventario")
    return inventario

def main():
    inventario = {'manzanas': 3, 'naranjas': 30, 'peras': 20}
    print("inventario: ", inventario)
    print("compro 2 manzanas, 1 pera y 1 naranja")
    productos_vendidos = ['manzanas', 'peras', 'manzanas', 'naranjas']
    inventario_actualizado = actualizar_inventario(inventario, productos_vendidos)
    print("inventario: ", inventario_actualizado)
    print("compro 1 manzana")
    productos_vendidos = ['manzanas']
    inventario_actualizado = actualizar_inventario(inventario, productos_vendidos)
    print("inventario: ", inventario_actualizado)



main()

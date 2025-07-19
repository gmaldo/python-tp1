def calcularDescuento(precio: float, porcentaje_descuento: float) -> float:
    """Calcula el precio final de un producto después de aplicar un descuento.

    Args:
        precio (float): El precio original del producto.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar.

    Returns:
        float: El precio final después de aplicar el descuento.
    """

    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento

def main():
    precio = float(input("Ingrese el precio del producto: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
    precio_final = calcularDescuento(precio, porcentaje_descuento)
    print(f"El precio final después de aplicar el descuento es: {precio_final:.2f}")

main()
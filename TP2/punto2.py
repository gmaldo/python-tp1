def convertirTemperatura(temperatura: float, unidad_origen: str, unidad_destino: str) -> float:
    """Convierte una temperatura entre Celsius y Fahrenheit.

    Args:
        temperatura (float): La temperatura a convertir.
        unidad_origen (str): La unidad de origen ('C' para Celsius, 'F' para Fahrenheit).
        unidad_destino (str): La unidad de destino ('C' para Celsius, 'F' para Fahrenheit).

    Returns:
        float: La temperatura convertida.

    Raises:
        ValueError: Si las unidades de origen o destino no son válidas.

    Ejemplos:
        >>> convertirTemperatura(0, 'C', 'F')
        32.0
        >>> convertirTemperatura(32, 'F', 'C')
        0.0
        >>> convertirTemperatura(100, 'C', 'F')
        212.0
        >>> convertirTemperatura(212, 'F', 'C')
        100.0
    """
    if unidad_origen.upper() == 'C' and unidad_destino.upper() == 'F':
        return (temperatura * 9/5) + 32 #(0 °C × 9/5) + 32 = 32 °F
    elif unidad_origen.upper() == 'F' and unidad_destino.upper() == 'C':
        return (temperatura - 32) * 5/9 #al verres
    else:
        raise ValueError("Unidades de origen o destino no válidas. Use 'C' o 'F'.")


def main():
     temp_celsius = 25
     temp_fahrenheit = convertirTemperatura(temp_celsius, 'C', 'F')
     print(f"{temp_celsius}°C es igual a {temp_fahrenheit}°F")

     temp_fahrenheit_2 = 68
     temp_celsius_2 = convertirTemperatura(temp_fahrenheit_2, 'F', 'C')
     print(f"{temp_fahrenheit_2}°F es igual a {temp_celsius_2}°C")

main()
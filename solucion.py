# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    resultado = []
    #Parte superior
    for i in range(m, 0, -2):
        espacio = (m - i) // 2
        resultado.append(" " * espacio + s * i)
        inicio = 2 if m % 2 == 0 else 3
    #Parte inferior
    for i in range(inicio, m + 1, 2):
        espacio = (m - i) // 2
        resultado.append(" " * espacio + s * i)
    print("\n".join(resultado))
    pass

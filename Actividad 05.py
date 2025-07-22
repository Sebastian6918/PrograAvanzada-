while True:
    print("MENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Buscar si una venta específica existe en la lista")
    print("7. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)")
    print("8. Salir")
    opcion = input("Ingrese una opción ")

    match opcion:
        case 1:
            print("")
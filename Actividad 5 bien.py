print("Análisis de ventas diarias")

ventas = []

while True:
    print("\nMENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar lista de ventas")
    print("2. Mostrar todas las ventas")
    print("3. Ver venta más alta y más baja")
    print("4. Ver promedio de ventas")
    print("5. Contar días con ventas mayores a Q1000")
    print("6. Clasificar cada venta")
    print("7. Salir")

    opcion = input("Elegí una opción (1-7): ")

    match opcion:
        case "1":
            ventas.clear()
            while True:
                dias = input("¿Cuántos días querés registrar? (mínimo 1): ")
                if dias.isdigit() and int(dias) > 0:
                    n = int(dias)
                    for i in range(n):
                        while True:
                            val = input("Venta del día " + str(i + 1) + ": Q")
                            if val.isdigit() and int(val) >= 0:
                                ventas.append(int(val))
                                break
                            else:
                                print("Error: Ingresá un número entero positivo")
                    break
                else:
                    print("Error: Debes ingresar un número entero positivo (1 o más)")

        case "2":
            if not ventas:
                print("Todavía no ingresaste ventas")
            else:
                print("Ventas registradas:")
                for i, v in enumerate(ventas, 1):
                    print(f"Día {i}: Q{v:,.2f}")

        case "3":
            if not ventas:
                print("No hay datos cargados")
            else:
                mayor = max(ventas)
                menor = min(ventas)
                print(f"Venta más alta: Q{mayor:,.2f}")
                print(f"Venta más baja: Q{menor:,.2f}")

        case "4":
            if not ventas:
                print("No hay ventas para sacar promedio")
            else:
                prom = sum(ventas) / len(ventas)
                print(f"Promedio de ventas: Q{prom:,.2f}")

        case "5":
            if not ventas:
                print("No hay datos cargados")
            else:
                cont = sum(1 for v in ventas if v > 1000)
                print(f"Días con ventas mayores a Q1,000: {cont}")

        case "6":
            if not ventas:
                print("Primero tenés que ingresar ventas")
            else:
                for i, v in enumerate(ventas, 1):
                    if v > 1000:
                        clasif = "Venta alta"
                    elif v >= 500:
                        clasif = "Venta media"
                    else:
                        clasif = "Venta baja"
                    print(f"Día {i}: Q{v:,.2f} → {clasif}")

        case "7":
            print("Chau, gracias por usar el programa")
            break

        case _:
            print("Error: Esa opción no existe")
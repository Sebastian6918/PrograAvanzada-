def saludar():
    print("Bienvenido al programa :)")

def pedir_numeros(n, tipo=float):
    lista = []
    for i in range(n):
        while True:
            valor = input(f"Ingrese el número {i + 1}: ")
            try:
                num = tipo(valor)
                lista.append(num)
                break
            except:
                print("Eso no es un número válido, intentá otra vez.")
    return lista

def suma_total(lista):
    return sum(lista)

def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def contar_signos(lista):
    pos = sum(1 for x in lista if x > 0)
    neg = sum(1 for x in lista if x < 0)
    ceros = sum(1 for x in lista if x == 0)
    return pos, neg, ceros

def multiplos_tres(lista):
    return sum(1 for x in lista if x % 3 == 0)

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def promedio_calificaciones(lista):
    if len(lista) == 0:
        return 0, 0, 0
    prom = sum(lista) / len(lista)
    altas = sum(1 for x in lista if x >= 85)
    riesgo = sum(1 for x in lista if x < 60)
    return prom, altas, riesgo

def mayor_menor(lista):
    if len(lista) == 0:
        return None, None
    return max(lista), min(lista)

def contar_repetidos(lista):
    rep = {}
    for x in lista:
        rep[x] = rep.get(x, 0) + 1
    return {k: v for k, v in rep.items() if v > 1}

def calculadora(a, b, op):
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        if b == 0:
            return "No se puede dividir entre cero"
        return a / b
    else:
        return "Operación inválida"

saludar()

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ingresar lista y mostrar suma, promedio, positivos, negativos, ceros, múltiplos de 3")
    print("2. Calcular área y perímetro de un rectángulo")
    print("3. Verificar si un número es primo")
    print("4. Promedio de calificaciones y conteos")
    print("5. Lista de enteros: mayor, menor y repetidos")
    print("6. Calculadora básica")
    print("7. Salir")

    opcion = input("Elegí una opción: ")

    match opcion:
        case "1":
            try:
                n = int(input("¿Cuántos números vas a ingresar? "))
                lista = pedir_numeros(n)
                print("Suma total:", suma_total(lista))
                print("Promedio:", promedio(lista))
                pos, neg, ceros = contar_signos(lista)
                print("Positivos:", pos, "Negativos:", neg, "Ceros:", ceros)
                print("Múltiplos de 3:", multiplos_tres(lista))
            except:
                print("Eso no es un número válido")
        case "2":
            try:
                base = float(input("Base del rectángulo: "))
                altura = float(input("Altura del rectángulo: "))
                print("Área:", area_rectangulo(base, altura))
                print("Perímetro:", perimetro_rectangulo(base, altura))
            except:
                print("Ingresá números válidos")
        case "3":
            try:
                num = int(input("Número para verificar si es primo: "))
                if es_primo(num):
                    print(f"{num} es primo")
                else:
                    print(f"{num} no es primo")
            except:
                print("Tenés que ingresar un número entero")
        case "4":
            try:
                n = int(input("¿Cuántas calificaciones querés ingresar? "))
                notas = pedir_numeros(n)
                prom, altas, riesgo = promedio_calificaciones(notas)
                print("Promedio:", prom)
                print("Calificaciones >= 85:", altas)
                print("Calificaciones en zona de riesgo (<60):", riesgo)
            except:
                print("Ingresá números válidos")
        case "5":
            try:
                n = int(input("¿Cuántos números enteros querés ingresar? "))
                lista = pedir_numeros(n, int)
                mayor, menor = mayor_menor(lista)
                print("Mayor:", mayor)
                print("Menor:", menor)
                repetidos = contar_repetidos(lista)
                if repetidos:
                    print("Números que se repiten con frecuencia:")
                    for k, v in repetidos.items():
                        print(f"  {k} se repite {v} veces")
                else:
                    print("No hay números repetidos")
            except:
                print("Ingresá datos válidos")
        case "6":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print("Operaciones:")
                print(" 1. Sumar")
                print(" 2. Restar")
                print(" 3. Multiplicar")
                print(" 4. Dividir")
                op = input("Elegí la operación (1-4): ")
                res = calculadora(a, b, op)
                print("Resultado:", res)
            except:
                print("Algo falló, revisá los datos")
        case "7":
            print("Gracias por usar el programa, hasta luego :)")
            break
        case _:
            print("Opción no válida, probá otra vez :)")

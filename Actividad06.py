def saludar():
    print("Bienvenido al programa :)")

def pedir_numeros(n):
    lista = []
    for _ in range(n):
        num = float(input("Ingrese un número: "))
        lista.append(num)
    return lista

def suma_promedio_signos(lista):
    suma = sum(lista)
    prom = suma / len(lista)
    pos = sum(1 for x in lista if x > 0)
    neg = sum(1 for x in lista if x < 0)
    return suma, prom, pos, neg


def atriangulo(a, b):
    return (a * b)/2

def es_par(numero):
    return numero % 2 == 0

def calificaciones(notas):
    return sum(notas) / len(notas)

def mayor_menor(lista):
    return max(lista), min(lista)

saludar()

while True:
    print("\n=== MENÚ ===")
    print("1. Ingresar n números y mostrar")
    print("2. Calcular el área de un triángulo")
    print("3. Verificar si un número es par")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n números y mostrar el mayor y el menor")
    print("6. Salir")

    opcion = input("Elija una opción (1-6): ")

    match opcion:
        case "1":
            n = int(input("¿Cuántos números quiere ingresar?: "))
            nums = pedir_numeros(n)
            suma, prom, pos, neg = suma_promedio_signos(nums)
            print("Suma total:", suma)
            print("Promedio:", prom)
            print("Positivos:", pos)
            print("Negativos:", neg)
        case "2":
            a = float(input("Ingrese la base: "))
            b = float(input("Ingrese la altura: "))
            resultado = atriangulo(a, b)
            print("El area del triangulo es:", resultado)

        case "3":
            numero = int(input("Ingrese un número: "))
            if es_par(numero):
                print("El número es par.")
            else:
                print("El número es impar")

        case "4":
            n = int(input("¿Cuántas calificaciones quiere ingresar?: "))
            notas = pedir_numeros(n)
            prom = calificaciones(notas)
            print("Promedio de calificaciones:", prom)

        case "5":
            n = int(input("¿Cuántos números quiere ingresar?: "))
            lista = pedir_numeros(n)
            mayor, menor = mayor_menor(lista)
            print("Mayor:", mayor)
            print("Menor:", menor)
        case "6":
            print("Gracias por usar el programa :)")
            break
        case _:
            print("Opción no válida. Intente nuevamente")
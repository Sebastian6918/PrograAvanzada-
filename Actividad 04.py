1. Simulador de votación
print("Formulario de votación")

nombre = input("Escribe tu nombre completo: ")
dpi = input("Escribe tu DPI (13 números): ")
dep = input("¿En qué departamento vives?: ")
nac = input("¿En qué año naciste?: ")

if len(nombre) < 5:
    print("Ese nombre es muy corto.")
elif len(dpi) != 13 or not dpi.isdigit():
    print("Ese DPI no sirve.")
elif not nac.isdigit():
    print("Eso no parece un año.")
else:
    edad = 2025 - int(nac)
    if (dep.lower() == "petén" or dep.lower() == "alta verapaz") and edad >= 17:
        print("Puedes votar.")
        print("Hola " + nombre + ", tu centro de votación está en " + dep)
    elif edad >= 18:
        print("Puedes votar.")
        print("Hola " + nombre + ", tu centro de votación está en " + dep)
    else:
        print("Todavía no puedes votar.")

2. Calculadora de impuestos
print("Calculadora de impuestos")

dinero = input("¿Cuánto ganas al año?: ")
fam = input("¿Cuántas personas dependen de ti?: ")

if not dinero.isdigit() or not fam.isdigit():
    print("Esos datos no sirven.")
else:
    ingreso = int(dinero)
    dep = int(fam)
    desc = dep * 1000
    imp = 0

    if ingreso < 40000 and dep > 2:
        imp = 0
    else:
        if ingreso <= 30000:
            imp = ingreso * 0.05
        elif ingreso <= 60000:
            imp = ingreso * 0.10
        elif ingreso <= 100000:
            imp = ingreso * 0.15
        else:
            imp = ingreso * 0.20

        imp = imp - desc
        if imp < 0:
            imp = 0

    print("Tienes que pagar: Q" + str(int(imp)))

3. Sistema de autenticación
print("Iniciar sesión")

intentos = 0
usuario1 = "luis"
clave1 = "1234"
usuario2 = "ana"
clave2 = "abcd"
usuario3 = "mario"
clave3 = "pass"

acceso = False

while intentos < 3:
    user = input("Usuario: ")
    passw = input("Contraseña: ")

    if (user == usuario1 and passw == clave1) or (user == usuario2 and passw == clave2) or (user == usuario3 and passw == clave3):
        acceso = True
        break
    else:
        print("Datos incorrectos.")
        intentos = intentos + 1

if acceso:
    print("Bienvenido", user)
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")
else:
    print("ACCESO BLOQUEADO")

4. Simulador de facturación
print("Simulador de facturación")

suma = 0
seguir = "s"

while seguir == "s":
    num = input("Precio del producto: ")
    if num.isdigit():
        suma = suma + int(num)
    else:
        print("Eso no es un número.")
    seguir = input("¿Quieres agregar otro? (s/n): ")

prop = input("¿Quieres dejar propina? (s/n): ")
porc = 0

if prop == "s":
    cant = input("¿Cuánto porcentaje de propina?: ")
    if cant.isdigit():
        porc = int(cant)

descuento = 0
cliente = input("¿Tienes tarjeta de cliente frecuente? (s/n): ")
if cliente == "s":
    descuento = suma * 0.10

iva = suma * 0.12
propina = suma * (porc / 100)
total = suma + iva + propina - descuento

print("--------- Factura ---------")
print("Subtotal: Q" + str(suma))
print("IVA (12%): Q" + str(int(iva)))
print("Propina: Q" + str(int(propina)))
print("Descuento: Q" + str(int(descuento)))
print("Total a pagar: Q" + str(int(total)))

5. Verificador de fecha válida y día de la semana
print("Verificador de fecha")

dia = input("Día: ")
mes = input("Mes: ")
año = input("Año: ")

if not dia.isdigit() or not mes.isdigit() or not año.isdigit():
    print("Eso no es una fecha.")
else:
    d = int(dia)
    m = int(mes)
    a = int(año)

    if m < 1 or m > 12 or d < 1 or d > 31:
        print("Esa fecha no existe.")
    elif m == 2 and d > 29:
        print("Febrero no tiene tantos días.")
    elif (m in [4, 6, 9, 11]) and d > 30:
        print("Ese mes no tiene 31 días.")
    else:
        if m < 3:
            m = m + 12
            a = a - 1

        k = a % 100
        j = a // 100

        f = d + 13*(m+1)//5 + k + k//4 + j//4 + 5*j
        dia_sem = f % 7

        nombre = ""

        if dia_sem == 0:
            nombre = "sábado"
        elif dia_sem == 1:
            nombre = "domingo"
        elif dia_sem == 2:
            nombre = "lunes"
        elif dia_sem == 3:
            nombre = "martes"
        elif dia_sem == 4:
            nombre = "miércoles"
        elif dia_sem == 5:
            nombre = "jueves"
        elif dia_sem == 6:
            nombre = "viernes"

        print("La fecha " + dia + "/" + mes + "/" + str(a + 1 if m > 12 else a) + " fue un " + nombre)

 6. Clasificador de envío
print("Clasificador de envío")

peso = input("¿Cuánto pesa el paquete (kg)?: ")
dist = input("¿Cuántos km hay hasta el destino?: ")
urge = input("¿Es urgente? (s/n): ")
tam = input("¿Tamaño del paquete? (pequeño/mediano/grande): ")

if not peso.isdigit() or not dist.isdigit():
    print("Datos incorrectos.")
else:
    p = int(peso)
    d = int(dist)
    base = p * 2 + d * 0.5
    extra = 0
    desc = 0

    if urge == "s":
        extra = extra + 50
    if tam == "grande":
        extra = extra + 30
    if urge == "n" and p < 5:
        desc = 20

    total = base + extra - desc

    print("----- Detalle -----")
    print("Base: Q" + str(int(base)))
    print("Recargos: Q" + str(int(extra)))
    print("Descuento: Q" + str(int(desc)))
    print("Total a pagar: Q" + str(int(total)))

7. Sistema de calificaciones con curva
print("Notas de estudiantes")

nombres = []
proms = []

curva = False

for i in range(5):
    print("Estudiante", i + 1)
    nom = input("Nombre: ")

    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    n3 = int(input("Nota 3: "))

    prom = (n1 + n2 + n3) / 3

    if prom < 70:
        curva = True

    nombres.append(nom)
    proms.append([n1, n2, n3])

if curva:
    print("Se aplicará curva")
    for i in range(5):
        for j in range(3):
            nota = proms[i][j]
            nueva = nota + 5
            if nueva > 100:
                nueva = 100
            proms[i][j] = nueva

print("----- Promedios -----")
for i in range(5):
    suma = proms[i][0] + proms[i][1] + proms[i][2]
    final = suma / 3
    print(nombres[i] + ": " + str(int(final)))

8. Calculadora de rumbo entre puntos cardinales
print("Calculadora de dirección")

a = input("¿Desde dónde partes? (norte/sur/este/oeste): ")
b = input("¿Hacia dónde vas? (norte/sur/este/oeste): ")

if a == b:
    print("Ya estás en ese lugar.")
elif a == "norte":
    if b == "sur":
        print("Recto hacia el sur")
    elif b == "este":
        print("Debes ir hacia noreste")
    elif b == "oeste":
        print("Debes ir hacia noroeste")
elif a == "sur":
    if b == "norte":
        print("Recto hacia el norte")
    elif b == "este":
        print("Debes ir hacia sureste")
    elif b == "oeste":
        print("Debes ir hacia suroeste")
elif a == "este":
    if b == "oeste":
        print("Recto hacia el oeste")
    elif b == "norte":
        print("Debes ir hacia noreste")
    elif b == "sur":
        print("Debes ir hacia sureste")
elif a == "oeste":
    if b == "este":
        print("Recto hacia el este")
    elif b == "norte":
        print("Debes ir hacia noroeste")
    elif b == "sur":
        print("Debes ir hacia suroeste")
else:
    print("Dirección no válida")

9. Simulador de entradas al cine
print("Entradas al cine")

edad = input("¿Cuántos años tienes?: ")
dia = input("¿Qué día es hoy?: ")
est = input("¿Eres estudiante? (s/n): ")

if not edad.isdigit():
    print("Edad inválida.")
else:
    e = int(edad)

    if e < 13:
        print("No puedes entrar a películas para mayores de 15.")
    else:
        precio = 50

        if est == "s":
            precio = 35

        if dia.lower() == "miércoles":
            print("Promo 2x1 activa hoy")
            print("Precio por 2 personas: Q" + str(precio))
        else:
            print("Tu entrada cuesta: Q" + str(precio))

10. Comparador de fechas
print("Comparador de fechas")

d1 = input("Día primera fecha: ")
m1 = input("Mes primera fecha: ")
a1 = input("Año primera fecha: ")

d2 = input("Día segunda fecha: ")
m2 = input("Mes segunda fecha: ")
a2 = input("Año segunda fecha: ")

if not (d1.isdigit() and m1.isdigit() and a1.isdigit() and d2.isdigit() and m2.isdigit() and a2.isdigit()):
    print("Datos inválidos.")
else:
    d1 = int(d1)
    m1 = int(m1)
    a1 = int(a1)
    d2 = int(d2)
    m2 = int(m2)
    a2 = int(a2)

    def total_dias(d, m, a):
        meses = [31,28,31,30,31,30,31,31,30,31,30,31]
        tot = a * 365 + d
        for i in range(m - 1):
            tot += meses[i]

        tot += (a // 4)
        return tot

    t1 = total_dias(d1,m1,a1)
    t2 = total_dias(d2,m2,a2)

    if t1 > t2:
        print("La primera fecha es mayor.")
    elif t2 > t1:
        print("La segunda fecha es mayor.")
    else:
        print("Ambas fechas son iguales.")

    if m1 == m2 and a1 == a2:
        print("Están en el mismo mes y año.")
    else:
        print("No están en el mismo mes y año.")

    dif = t1 - t2
    if dif < 0:
        dif = -dif

    print("Han pasado " + str(dif) + " días entre ambas fechas.")

# DRY (Don't Repeat Yourself)
print("==== FUNCIONES ====")


def saludar(nombre):
    print(f"Hola me llamo {nombre}")


saludar("Linder")


def sumar(n1=0, n2=0):
    print(f"n1 {n1} n2 {n2}")
    return n1 + n2


print(sumar(30, 15))
print(sumar(n2=10, n1=20))


def saludar2(nombre, apellido, edad):
    print(f"Hola me llamo {nombre} {apellido} y tengo {edad} años de edad")


saludar2("Pepe", "Perez", 30)
saludar2(edad=25, nombre="Juan", apellido="Zapata")

print("==== ARGS ====")


def average(*notas):
    print(notas)
    suma = 0
    for nota in notas:
        suma += nota
    print(suma / len(notas))


average(10, 20, 17, 18)
average(19)
print("-" * 40)

print("==== Kwargs ====")


def persona(**datos):
    # Diccion key:value
    print(datos)
    print("====KEYS====")
    for key in datos.keys():
        print(key)

    print("====VALUES====")
    for values in datos.values():
        print(values)

    print("====ITEMS====")
    for key, value in datos.items():
        print(key, value)


persona(
    name="Linder",
    lastname="Hassinger",
    phone_number="99999",
    dni=88888,
    age=55,
    is_developer=True
)

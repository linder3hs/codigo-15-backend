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

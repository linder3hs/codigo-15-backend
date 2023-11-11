print("==== VARIABLES ====")
nombre = "Linder" # string
apellido = "Hassinger"
numero1 = 10 # int
numero2 = 100.46 # float
es_mayor = True # bool
es_presidente = False # bool

print(nombre, numero1, numero2)
print("Hola mi nombres es " + nombre + " " + apellido + ", saludos")
# f string
print(f"Hola mi nombre es {nombre} {apellido}, saludos")
print(nombre + str(numero1))
print(numero1 + numero2)
# print(nombre - str(numero1))
print("-" * 50)
print("==== LISTAS ====")
teams = ["Bacelona", "Real Madrid", "PSG", "Boca JR", ["Messi", "CR7", "Mbape", "Pepe"]]
print(teams[4][2])
tv_shows = ["Spiderman", "The big banh theory", "Moises"]
print(tv_shows)
tv_shows.append("Black Miror")
print(tv_shows)
tv_shows.append(["Breaking Bad", "Batman"])
print(tv_shows)

movies = ["Avengers", "Marvels", "Shazan"]
tv_shows.extend(movies)
print(tv_shows)

tv_shows.remove("Spiderman")
print(tv_shows)
tv_shows.pop()
print(tv_shows)
tv_shows.pop(4)
print(tv_shows)
tv_shows[3].pop(0)
print(tv_shows)
print(tv_shows.index("Black Miror"))

print("-" * 50)
print("===== TUPLAS ====")
months = ("Enero", "Febrero", "Marzo")
print(len(months))
print(len("Hola mundo"))

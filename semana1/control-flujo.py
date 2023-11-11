age = 18

if age >= 18:
  print("Mayor de edad")
else:
  print("Menor de edad")

price = 500
has_card = True

if has_card:
  print(price - 100)
elif price < 1000:
  print(price - 50)
else:
  print(price - 10)

colors = ["Yellow", "Red", "Brown", "Black", "White"]

print("==== FOR IN ====")
# for (let i = 0; i < colors.length; i ++)
# for (let variable of array)

for colorcito in colors:
  print(colorcito) 

teams = [
  "Bacelona", 
  "Real Madrid", 
  "PSG",
  "Boca JR", 
  ["Messi", "CR7", "Mbape", "Pepe"]
]

players = teams[4]

for player in players:
  print(player)

print("=== RANGE ===")
numbers = range(11)
print(list(numbers))
print("-"*40)
numbers2 = range(10, 21)
print(list(numbers2))
print("-"*40)
numbers3 = range(20, 10, -3)
print(list(numbers3))

for number in range(1, 10):
  if number % 2 == 0:
    print(f"{number} es par")
  else:
    print(f"{number} es impar")

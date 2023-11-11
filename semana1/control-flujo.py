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
  "PSG", "Boca JR", 
  ["Messi", "CR7", "Mbape", "Pepe"]
]

players = teams[3]

for player in players:
  print(player)

# una clase siempre inicia con mayuscula
class Person:
    """
      constructor
      es la funcion que se llama cuando se instancia a la clase, esta funcion 
      tiene un nombre especial __init__, esta siempre simpre tendra como primer 
      parametro a self
    """
    def __init__(self, name, lastname, phone_number, age):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.age = age

    
    def saludar(self):
        print(f"Hola me llamo {self.name} {self.lastname} ,mi numero es {self.phone_number} y tengo {self.age} años de edad")

  
#El llamar a una clase se la dice instanciar
persona1 = Person("Pepe", "Zapata", 99999, 52)
persona1.saludar()

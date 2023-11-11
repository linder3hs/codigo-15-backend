# una clase siempre inicia con mayuscula
class Person:
    """
      constructor
      es la funcion que se llama cuando se instancia a la clase, esta funcion 
      tiene un nombre especial __init__, esta siempre simpre tendra como primer 
      parametro a self
    """

    def __init__(self, name, lastname, phone_number, age, dni):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.age = age
        # es una variable privada
        self.__dni = dni

    def saludar(self):
        print(
            f"Hola me llamo {self.name} {self.lastname} ,mi numero es {self.phone_number} y tengo {self.age} años de "
            f"edad")

    def get_fullname(self):
        return f"{self.name} {self.lastname}"

    def format_phone_number(self):
        return f"+51{self.phone_number}"

    def get_dni(self):
        return self.__dni


# El llamar a una clase se la dice instanciar
persona1 = Person("Pepe", "Zapata", 99999, 52, "72812143")
persona1.phone_number = 989652132
persona1.saludar()
print(persona1.format_phone_number())
print(persona1.get_dni())

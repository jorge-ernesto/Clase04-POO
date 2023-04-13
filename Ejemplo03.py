class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Metodo para devolver una representacion de cadena de su objeto (clase definida por el usuario)
    def __str__(self):
        return self.color + ", " + str(self.ruedas)

class Automovil(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Metodo para devolver una representacion de cadena de su objeto (clase definida por el usuario)
    def __str__(self):
        return Vehiculo.__str__(self) + ", " + str(self.velocidad)

auto = Automovil("Azul", 4, 100)
print(auto)
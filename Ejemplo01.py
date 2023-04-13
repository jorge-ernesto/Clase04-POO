# definicion de una clase
class Clase01:
    x = 1
    y = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Metodo para devolver una representacion de cadena de su objeto (clase definida por el usuario)
    def __str__(self):
        # return "x="+str(self.x) + ", " + "y="+str(self.y)
        return str(self.__dict__)

    def sumar(self):
        print("Suma=", self.x + self.y)

# creacion de objetos, instanciamiento de la clase
obj1 = Clase01(1, 2)
obj2 = Clase01(3, 4)

print("---- Objeto 1 ----")
print(obj1.x)
print(obj1.y)
print(obj1)
obj1.x=5
print(obj1)
obj1.sumar()

print("---- Objeto 2 ----")
print(obj2.x)
print(obj2.y)
print(obj2)
obj2.sumar()

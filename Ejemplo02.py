class Persona:
    def __init__(self, nombre="SIN NOMBRE",edad=0,dni="9999999"):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Metodo para devolver una representacion de cadena de su objeto (clase definida por el usuario)
    def __str__(self):
        return str(self.__dict__)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            self.__edad = 0
        else:
            self.__edad = edad

    def esMayorEdad(self):
        return self.edad >= 18

per1 = Persona("Ernesto", -5, "7777777")
print(per1)

print(per1.esMayorEdad())

per1.nombre = "Miranda"
per1.edad = 20
print(per1)
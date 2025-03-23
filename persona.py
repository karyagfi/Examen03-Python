class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def leer(self, libro = "una revista"):
        print(f"{self.nombre} está leyendo {libro}.")
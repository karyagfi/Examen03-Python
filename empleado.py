class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def detalles(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")
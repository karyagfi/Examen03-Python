from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def detalles(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}, gerente de Departamento: {self.departamento}")
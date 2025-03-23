from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor

    def acelerar(self):
        print(f'El {self.modelo} de {self.marca} está acelerando.')

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f'La camioneta {self.modelo} de {self.marca} está acelerando.')

class Conductor:
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre
        self.vehiculo = vehiculo

    def conducir(self):
        print(f'{self.nombre} está conduciendo un {self.vehiculo.modelo}')
        self.vehiculo.acelerar()
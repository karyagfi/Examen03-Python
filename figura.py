from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2
    
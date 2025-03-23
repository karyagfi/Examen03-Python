# from persona import Persona
# from empleado import Empleado
# from gerente import Gerente
# from figura import Cuadrado
# from figura import Circulo
from lib.libro import Libro
from lib.biblioteca import Biblioteca
from cuenta import CuentaBancaria

# persona1 = Persona("Ana", 25)
# persona2 = Persona("Luis", 30)
# persona3 = Persona("Juan", 20)
# persona4 = Persona("Sofia", 25)
# persona5 = Persona("Carlos", 40)

# persona1.presentarse()
# persona2.presentarse()
# persona3.presentarse()
# persona4.presentarse()
# persona5.presentarse()


# persona1.leer("Grandes Esperanzas")
# persona1.leer("Frankenstein")
# persona2.leer("Metamorfosis")
# persona2.leer("Harry Potter y Camara Secreta")
# persona2.leer("Habitos Atomicos")

# e1 = Empleado("Fernanda", 1000)
# e2 = Empleado("Esmeralda", 1500)
# g1 = Gerente("Gustavo", 2000, "Sistemas")
# g2 = Gerente("Gabriela", 2500, "Ventas")

# e1.detalles()
# e2.detalles()  
# g1.detalles()
# g2.detalles()

# c1 = Cuadrado(5)
# c2 = Circulo(3) 

# print(c1.calcular_area())
# print(c2.calcular_area())

# libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
# libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
# libro3 = Libro("La Odisea", "Homero")

# biblioteca = Biblioteca()
# biblioteca.listar_libros()
# biblioteca.agregar_libro(libro1)
# biblioteca.agregar_libro(libro2)
# biblioteca.agregar_libro(libro3)
# biblioteca.listar_libros()

cuenta1 = CuentaBancaria("Ana", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
print(cuenta1.consultar_saldo())
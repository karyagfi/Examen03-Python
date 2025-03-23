class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    self.libros.append(libro)
    print(f"Se ha agregado el libro {libro.titulo} de {libro.autor}.")

  def listar_libros(self):
    if not self.libros:
        print("No hay libros en la biblioteca.")
    else:
      print("Catálogo de libros:")
      for libro in self.libros:
        print(f"{libro.info()}")
class Libro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def info(self):
    return f" El libro {self.titulo} del {self.autor}"
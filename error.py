class DimensionError(Exception):
  def __init__(self, mensaje="", dimension=None, maximo=None):
    super().__init__(mensaje)
    self.dimension = dimension
    self.maximo = maximo

  def __str__(self):
    if self.dimension is not None and self.maximo is not None:
      return f"{self.dimension} fuera de rango. {self.dimension} debe ser menor o igual a {self.maximo}."
    else:
      return super().__str__()
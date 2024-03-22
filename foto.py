from error import DimensionError

class Foto:
  MAX = 2500

  def __init__(self, ancho: int, alto: int, ruta: str) -> None:
    self.__ancho = ancho
    self.__alto = alto
    self.ruta = ruta

  @property
  def ancho(self) -> int:
    return self.__ancho

  @ancho.setter
  def ancho(self, ancho) -> None:
    if ancho < 1 or ancho > Foto.MAX:
      raise DimensionError(f"El ancho no puede ser menor a 1 o mayor a {Foto.MAX}", dimension="Ancho", maximo=Foto.MAX)
    else:
      self.__ancho = ancho

  @property
  def alto(self) -> int:
    return self.__alto

  @alto.setter
  def alto(self, alto) -> None:
    if alto < 1 or alto > Foto.MAX:
      raise DimensionError(f"El alto no puede ser menor a 1 o mayor a {Foto.MAX}", dimension="Alto", maximo=Foto.MAX)
    else:
      self.__alto = alto
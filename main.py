from foto import Foto
from error import DimensionError

def main():
  try:
    foto = Foto(5000, 7000, "ruta_predeterminada")
    print("Instancia de Foto creada con éxito.")
    foto.alto = 12000
  except DimensionError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    main()
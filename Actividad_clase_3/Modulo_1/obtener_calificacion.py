# Codigo con bug
# def obtener_calificacion(nota):
#     if nota >= 9:
#         return "Sobresaliente"
#     elif nota >= 7:
#         return "Notable"
#     elif nota >= 5:
#         return "Aprobado"
#     else:
#         return "Reprobado"

# print(obtener_calificacion(10))
# print(obtener_calificacion(8))
# print(obtener_calificacion(6))
# print(obtener_calificacion(4))

# Codigo corregido
def obtener_calificacion(nota):
    if not isinstance(nota, (int, float)) or not (0 <= nota <= 10):
        raise ValueError("La nota debe ser un número entre 0 y 10")
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Reprobado"
      
# Prueba unutaria
def test_obtener_calificacion():
  try:
      obtener_calificacion(11)
      assert False
  except ValueError:
      assert True
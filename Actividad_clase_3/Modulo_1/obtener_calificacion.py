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
#validar que sea del 1 al 10 y qeu no sea letra, que no sea una lista

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
    print("Error")
    assert True
      
def test_nota_es_string():
  try:
        obtener_calificacion("diez")
        assert False, "Debería haber lanzado TypeError por string"
  except TypeError:
    print("Error")
    assert True

# Test 2: Lista lanza TypeError
def test_nota_es_lista():
    try:
        obtener_calificacion([10])
        assert False, "Debería haber lanzado TypeError por lista"
    except TypeError:
      print("Error")
      assert True

# Test 3: Booleano lanza TypeError
def test_nota_es_booleano():
    try:
        obtener_calificacion(True)
        assert False, "Debería haber lanzado TypeError por booleano"
    except TypeError:
      print("Error")
      assert True

# Test 4: Número fuera de rango lanza ValueError
def test_nota_fuera_de_rango():
    try:
        obtener_calificacion(11)
        assert False, "Debería haber lanzado ValueError por número mayor a 10"
    except ValueError:
      print("Error")
      assert True
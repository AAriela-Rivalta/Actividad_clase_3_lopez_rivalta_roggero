# Codigo con bug
# def buscar_producto(inventario, nombre):
#     for i, prod in enumerate(inventario):
#         if prod["nombre"] == nombre:
#             return i
#     return None


# Codigo corregido
def buscar_producto(inventario, nombre):
    for prod in inventario:
        if prod["nombre"] == nombre:
            return prod
    return None
  
print(buscar_producto(
  [
  {"nombre": "Teclado", "stock": 4},
  {"nombre": "Mouse", "stock": 3}
  ], "Teclado"
  ))  # Devuelve el diccionario del producto
  
# Prueba unutaria
def test_buscar_producto():
    producto = {"nombre": "Teclado", "stock": 4}
    inventario = [producto]
    assert buscar_producto(inventario, "Teclado") == producto
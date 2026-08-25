# Codigo con bug
# def agregar_producto(carrito=[], producto=""):
#     carrito.append(producto)
#     return carrito

# Codigo corregido
def agregar_producto(carrito=None, producto=""):
    if carrito is None:
        carrito = []
    carrito.append(producto)
    return carrito
  
# Prueba unutaria
def test_agregar_producto():
    primer_carrito = agregar_producto(producto="Libro")
    segundo_carrito = agregar_producto(producto="Lapiz")
    assert primer_carrito == ["Libro"]
    assert segundo_carrito == ["Lapiz"]
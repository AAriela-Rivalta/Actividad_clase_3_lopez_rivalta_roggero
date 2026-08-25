# Codigo con bug
# def actualizar_stock(producto, cantidad):
#     producto["stock"] += cantidad
#     return producto

# Codigo corregido
def actualizar_stock(producto, cantidad):
    nuevo_stock = producto["stock"] + cantidad
    if nuevo_stock < 0:
        raise ValueError("El stock no puede quedar en negativo")
    producto["stock"] = nuevo_stock
    return producto
  
# Prueba unutaria
def test_actualizar_stock():
    producto = {"nombre": "Mouse", "stock": 2}
    try:
        actualizar_stock(producto, -3)
        assert False
    except ValueError:
        assert producto["stock"] == 2
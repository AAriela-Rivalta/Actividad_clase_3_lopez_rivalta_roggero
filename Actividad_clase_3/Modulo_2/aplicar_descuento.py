# Codigo con bug
# def aplicar_descuento(precio, descuento):
#     precio_final = precio - (precio * descuento / 100)
#     iva = precio * 0.21
#     return precio_final + iva

# Codigo corregido
def aplicar_descuento(precio, descuento):
    if not (0 <= descuento <= 100):
        raise ValueError("El descuento debe estar entre 0 y 100")
    precio_final = precio - (precio * descuento / 100)
    iva = precio_final * 0.21
    return precio_final + iva
  
# Prueba unutaria
def test_aplicar_descuento():
    assert round(aplicar_descuento(100, 10), 2) == 108.90
# Codigo con bug
# def generar_reporte(inventario):
#     total = sum(p["precio"] * p["stock"] for p in inventario)
#     if total == 0.0:
#         return "Inventario vacio"
#     promedio = total / len(inventario)
#     return f"Total: {total}, Promedio: {promedio}"

# Codigo corregido
def generar_reporte(inventario):
    if not inventario:
        return "Inventario vacio"
    total = sum(p["precio"] * p["stock"] for p in inventario)
    promedio = total / len(inventario)
    return f"Total: {total}, Promedio: {promedio}"
  
# Prueba unutaria
def test_generar_reporte():
    inventario = [{"precio": 50, "stock": 0}]
    assert generar_reporte(inventario) == "Total: 0, Promedio: 0.0"
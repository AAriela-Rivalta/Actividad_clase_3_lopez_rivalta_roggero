# Codigo con bug
# def procesar_ventas(ventas, descuento_global):
    # ventas_ordenadas = ventas
    # ventas_ordenadas.sort(key=lambda x: x["monto"])
    # total = sum(v["monto"] for v in ventas_ordenadas)
    # promedio = total / len(ventas_ordenadas)
    # total_con_descuento = total * (1 - descuento_global / 100)
    # promedio_con_descuento = promedio * (1 - descuento_global / 100)
    # return {
    #     "total": total_con_descuento,
    #     "promedio": promedio_con_descuento,
    #     "cantidad": len(ventas_ordenadas)
    # }

# Codigo corregido
def procesar_ventas(ventas, descuento_global):
    if not ventas:
        return {"total": 0.0, "promedio": 0.0, "cantidad": 0}
    total = sum(v["monto"] for v in ventas)
    promedio = total / len(ventas)
    total_con_descuento = total * (1 - descuento_global / 100)
    promedio_con_descuento = promedio * (1 - descuento_global / 100)
    return {
        "total": total_con_descuento,
        "promedio": promedio_con_descuento,
        "cantidad": len(ventas)
    }
  
# Prueba unutaria
def test_procesar_ventas():
    ventas = [{"monto": 500}, {"monto": 100}]
    procesar_ventas(ventas, 10)
    assert ventas == [{"monto": 500}, {"monto": 100}]
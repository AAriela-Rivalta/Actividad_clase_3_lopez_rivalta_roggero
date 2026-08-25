# Codigo con bug
# def calcular_promedio(notas):
#     return sum(notas) / len(notas)

# Codigo corregido
def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return sum(notas) / len(notas)
  
# Prueba unutaria
def test_calcular_promedio():
    try:
        calcular_promedio([])
        assert False
    except ValueError:
        assert True
    
  
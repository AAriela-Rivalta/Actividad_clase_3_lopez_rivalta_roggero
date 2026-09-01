# Codigo con bug
# def calcular_promedio(notas):
#     return sum(notas) / len(notas)
#print(calcular_promedio([8, 9, 10]))
# tiene que ser un array

# Codigo corregido
def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    for nota in notas:
        if not isinstance(nota, (int, float)) or isinstance(nota, bool):
            raise TypeError(f"Todas las notas deben ser numéricas. Se encontró: {type(nota).__name__}")
    return sum(notas) / len(notas)
  
# Prueba unutaria
def test_calcular_promedio():
    try:
        calcular_promedio([])
        assert False
    except ValueError:
        assert True
        
test_calcular_promedio()
# otra prueba podria ser que se le pase una letra en vez de un numero, y que se lance un error
    
  
# Codigo con bug
# def validar_horario(hora_inicio, hora_fin):
#     inicio = int(hora_inicio.split(":")[0]) * 60 + int(hora_inicio.split(":")[1])
#     fin = int(hora_fin.split(":")[0]) * 60 + int(hora_fin.split(":")[1])
#     if 0 <= inicio <= 1440 and 0 <= fin <= 1440:
#         return True
#     return False

# Codigo corregido
def validar_horario(hora_inicio, hora_fin):
    try:
        h_ini, m_ini = map(int, hora_inicio.split(":"))
        h_fin, m_fin = map(int, hora_fin.split(":"))
    except (ValueError, AttributeError):
        return False

    if not (0 <= h_ini < 24 and 0 <= m_ini < 60 and 0 <= h_fin < 24 and 0 <= m_fin < 60):
        return False

    inicio = h_ini * 60 + m_ini
    fin = h_fin * 60 + m_fin

    return inicio < fin
  
# Prueba unutaria
def test_validar_horario():
    assert validar_horario("17:00", "08:00") is False
    assert validar_horario("08:00", "17:00") is True
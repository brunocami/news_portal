import datetime

def obtener_hora_actual():
    hora_actual = datetime.datetime.now().isoformat(timespec='seconds')
    return hora_actual + "+00:00"


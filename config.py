def tipovehiculo(tipo):
    if tipo == 1:
        return 3500
    elif tipo == 2:
        return 4000
    elif tipo == 3:
        return 3000
    else:
        return 0 

def calculartiempo(horaentrada, minutosentrada, horasalida, minutossalida):
    minutostotalentrada = (horaentrada * 60) + minutosentrada
    minutostotalsalida = (horasalida * 60) + minutossalida

    diferencia = minutostotalsalida - minutostotalentrada

    if diferencia < 0:
        diferencia = diferencia + 1440

    return diferencia 

def convertirhoras(minutostotales):
    horasenteras = minutostotales // 60
    restominutos = minutostotales % 60

    if restominutos > 0:
        return horasenteras + 1
    else:
        return horasenteras

def calcular_importe(tipo, hora_ingreso, hora_egreso):
    preciohora = tipovehiculo(tipo)
    
    if preciohora == 0:
        return "tipo de vehiculo invalido"

    horaentrada = hora_ingreso.hour
    minutosentrada = hora_ingreso.minute
    horasalida = hora_egreso.hour
    minutossalida = hora_egreso.minute

    minutos = calculartiempo(horaentrada, minutosentrada, horasalida, minutossalida)
    
    horasdeestadia = convertirhoras(minutos)

    if horasdeestadia <= 1:
        return 0, 0
    else:
        horascobradas = horasdeestadia
        totalpagar = horascobradas * preciohora
        return horascobradas, totalpagar
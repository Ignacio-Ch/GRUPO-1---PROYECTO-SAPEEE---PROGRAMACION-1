"""
main.py
-------
Punto de entrada del sistema SAPE. Contiene el menú principal por
consola que conecta la lógica de negocio (estacionamiento.py,
reportes-consultas.py, validar.py) con la presentación (vista.py).

Ejecutar con:  python main.py
"""
#SECCION 1: IMPORTS

from config import FILAS, COLUMNAS
from validaciones import es_patente_valida
import estacionamiento as est
import reportes as rep
import vista

# SECCION 2: FUNCIONES AUXILIARES

def pedir_patente():
    patente = input("Ingrese la patente: ")
    
    if es_patente_valida(patente) == False:
        print("Patente inválida. Formatos aceptados: ABC123, abc123, AB123CD o ab123cd.")
        return None
    else:
        return patente

def pedir_tipo_vehiculo():
    """
    Solicita al usuario que seleccione el tipo de vehículo mediante un número.
    Retorna "1", "2" o "3" según la selección.
    """
    print("Seleccione el tipo de vehículo: 1 - Auto, 2 - Camioneta 3 - Moto")

    opcion = input("Ingrese el número (1, 2 o 3): ")
    
    if opcion == "1" or opcion == "2" or opcion == "3":
        return opcion
    else:
        print("Opción inválida. Debe ser 1, 2 o 3.")
        return None

#SECCION 3: OPCIONES DEL MENU

# Opción 1: registra el ingreso de un vehículo al estacionamiento
def opcion_registrar_ingreso(matriz, registros):
    patente = pedir_patente()
    if patente == None:
        return

    tipo = pedir_tipo_vehiculo()
    if tipo == None:
        return

    ok, datos = est.registrar_ingreso(matriz, registros, patente, tipo)
    if ok == True:
        fila, columna = datos
        print("Ingreso registrado. Espacio asignado: fila", fila, ", columna", columna)
    else:
        print("No se pudo registrar el ingreso:", datos)


# Opción 2: registra el egreso de un vehículo y muestra el ticket
def opcion_registrar_egreso(matriz, registros, historial):
    patente = pedir_patente()
    if patente == None:
        return

    ok, datos = est.registrar_egreso(matriz, registros, historial, patente)
    if ok == True:
        vista.mostrar_ticket(datos)
    else:
        print("No se pudo registrar el egreso:", datos)
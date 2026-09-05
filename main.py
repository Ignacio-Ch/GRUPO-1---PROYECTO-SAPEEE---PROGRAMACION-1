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
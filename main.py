"""
main.py
-------
Punto de entrada del sistema SAPE. Contiene el menú principal por
consola que conecta la lógica de negocio (estacionamiento.py,
reportes-consultas.py, validar.py) con la presentación (vista.py).

Ejecutar con:  python main.py
"""

from config import FILAS, COLUMNAS, TARIFAS, TIPOS_VEHICULOS
from validaciones import es_patente_valida
import estacionamiento as est
import reportes as rep
import vista
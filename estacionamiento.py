"""
estacionamiento.py
-------------------
Lógica central del sistema: manejo de la matriz de espacios,
registro de ingresos/egresos y cálculo de tarifas.

Estructuras de datos utilizadas:
    matriz:     lista de listas. Cada celda vale None si el espacio
                está libre, o la patente del vehículo si está ocupado.
    registros:  diccionario  patente -> {
                    "tipo": str,
                    "hora_ingreso": datetime,
                    "espacio": (fila, columna)
                }
    historial:  lista de diccionarios (tickets) con los egresos ya
                facturados:
                {
                    "patente": str,
                    "tipo": str,
                    "hora_ingreso": datetime,
                    "hora_egreso": datetime,
                    "horas_cobradas": int,
                    "importe": float,
                }
"""

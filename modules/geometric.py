import pandas as pd
import numpy as np


def geometric_analysis(ruta_datos):
    """
    Realiza el análisis geométrico de las ubicaciones de las atracciones.

    Tareas realizadas:
    1. Calcular las distancias entre atracciones.
    2. Determinar los puntos medios entre atracciones para ubicar puestos de servicio.
    3. Identificar las rectas entre atracciones, paralelas y perpendiculares.

    :param ruta_datos: Ruta al archivo CSV con los datos del parque.
    :return: DataFrame con resultados del análisis geométrico.
    """
    # Cargar datos
    datos = pd.read_csv(ruta_datos)

    # Calcular distancias entre atracciones
    datos['distancia'] = np.sqrt((datos['coord_x'].diff()) ** 2 + (datos['coord_y'].diff()) ** 2)

    # Calcular puntos medios entre atracciones
    datos['punto_medio_x'] = (datos['coord_x'] + datos['coord_x'].shift()) / 2
    datos['punto_medio_y'] = (datos['coord_y'] + datos['coord_y'].shift()) / 2

    # Calcular pendiente y ecuaciones de rectas
    datos['pendiente'] = (datos['coord_y'].diff()) / (datos['coord_x'].diff())
    datos['recta'] = datos['pendiente'] * datos['coord_x'] + datos['coord_y']

    # Identificar paralelas y perpendiculares
    datos['paralela'] = datos['pendiente'].duplicated()
    datos['perpendicular'] = datos['pendiente'] * datos['pendiente'].shift() == -1

    return datos
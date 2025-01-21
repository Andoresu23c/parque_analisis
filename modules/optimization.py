import pandas as pd


def function_optimization(ruta_datos):
    """
    Realiza el análisis de optimización y modelado de funciones relacionadas con las atracciones.

    Tareas realizadas:
    1. Modelar la función de velocidad para las atracciones.
    2. Calcular límites de la función de velocidad.
    3. Verificar la continuidad de la función en puntos críticos.
    4. Calcular la derivada primera (velocidad instantánea).
    5. Calcular la derivada segunda (aceleración).
    6. Identificar puntos máximos y mínimos de velocidad.

    :param ruta_datos: Ruta al archivo CSV con los datos del parque.
    :return: DataFrame con resultados del análisis de optimización.
    """
    # Cargar datos
    datos = pd.read_csv(ruta_datos)

    # Modelar la función de velocidad (ejemplo: v(t) = at² + bt + c)
    a, b, c = 2, 3, 5  # Coeficientes de la función de velocidad
    datos['velocidad_modelada'] = a * datos['tiempo_ciclo'] ** 2 + b * datos['tiempo_ciclo'] + c

    # Calcular límites de la función en puntos específicos
    datos['limite_izquierdo'] = datos['velocidad_modelada'].shift(1)
    datos['limite_derecho'] = datos['velocidad_modelada'].shift(-1)

    # Verificar continuidad
    datos['es_continua'] = datos['velocidad_modelada'] == datos['limite_derecho']

    # Calcular derivadas
    datos['velocidad_instantanea'] = 2 * a * datos['tiempo_ciclo'] + b  # Primera derivada
    datos['aceleracion'] = 2 * a  # Segunda derivada constante

    # Identificar puntos máximos y mínimos
    datos['es_maximo'] = (datos['velocidad_instantanea'].shift(1) > datos['velocidad_instantanea']) & \
                         (datos['velocidad_instantanea'].shift(-1) < datos['velocidad_instantanea'])
    datos['es_minimo'] = (datos['velocidad_instantanea'].shift(1) < datos['velocidad_instantanea']) & \
                         (datos['velocidad_instantanea'].shift(-1) > datos['velocidad_instantanea'])

    return datos
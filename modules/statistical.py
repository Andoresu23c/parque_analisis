import pandas as pd
import numpy as np


def statistical_analysis(ruta_datos):
    """
    Realiza el análisis estadístico de los datos relacionados con visitantes y tiempos de espera.

    Tareas realizadas:
    1. Calcular estadísticas descriptivas (media, mediana, moda, varianza, desviación estándar).
    2. Analizar la distribución de visitantes por hora.
    3. Calcular correlación entre tiempos de espera y número de visitantes.
    4. Generar una ecuación de regresión lineal para predicciones.
    5. Calcular el coeficiente de determinación (R²).

    :param ruta_datos: Ruta al archivo CSV con los datos del parque.
    :return: DataFrame con resultados del análisis estadístico.
    """
    # Cargar datos
    datos = pd.read_csv(ruta_datos)

    # Estadísticas descriptivas de tiempos de espera
    datos['media_espera'] = datos['tiempo_espera'].mean()
    datos['mediana_espera'] = datos['tiempo_espera'].median()
    datos['moda_espera'] = datos['tiempo_espera'].mode()[0]

    # Varianza y desviación estándar de tiempos de operación
    datos['varianza_operacion'] = datos['tiempo_ciclo'].var()
    datos['desviacion_operacion'] = datos['tiempo_ciclo'].std()

    # Distribución de visitantes por hora
    visitantes_por_hora = datos.groupby('timestamp')['visitantes_cola'].sum().reset_index()

    # Calcular correlación
    correlacion = datos['visitantes_cola'].corr(datos['tiempo_espera'])
    datos['correlacion'] = correlacion

    # Calcular regresión lineal
    covarianza = np.cov(datos['visitantes_cola'], datos['tiempo_espera'])[0][1]
    varianza_espera = np.var(datos['tiempo_espera'])
    pendiente = covarianza / varianza_espera
    intercepto = datos['visitantes_cola'].mean() - pendiente * datos['tiempo_espera'].mean()
    datos['regresion_lineal'] = pendiente * datos['tiempo_espera'] + intercepto

    # Calcular coeficiente de determinación (R²)
    datos['r_cuadrado'] = correlacion ** 2

    return datos
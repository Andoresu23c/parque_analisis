from config import data_path
from modules.geometric import geometric_analysis
from modules.optimization import function_optimization
from modules.statistical import statistical_analysis
from tqdm import tqdm

def main():
    """
    Función principal para ejecutar todos los análisis del parque de diversiones.
    """
    print("=== INICIO DEL PROCESO ===")

    # 1. Cargar los datos
    print("Cargando datos...")
    ruta_datos = data_path

    # 2. Realizar el análisis geométrico
    print("Realizando análisis geométrico...")
    for _ in tqdm(range(1), desc="Análisis geométrico"):
        resultados_geometricos = geometric_analysis(ruta_datos)

    # 3. Realizar el análisis de optimización de funciones
    print("Realizando análisis de optimización de funciones...")
    for _ in tqdm(range(1), desc="Optimización de funciones"):
        resultados_optimizacion = function_optimization(ruta_datos)

    # 4. Realizar el análisis estadístico
    print("Realizando análisis estadístico...")
    for _ in tqdm(range(1), desc="Análisis estadístico"):
        resultados_estadisticos = statistical_analysis(ruta_datos)

    # 5. Guardar los resultados en la carpeta 'data'
    print("Guardando resultados...")
    with tqdm(total=3, desc="Guardando resultados") as pbar:
        resultados_geometricos.to_csv("data/analisis_geometrico.csv", index=False)
        pbar.update(1)
        resultados_optimizacion.to_csv("data/optimizacion_funciones.csv", index=False)
        pbar.update(1)
        resultados_estadisticos.to_csv("data/analisis_estadistico.csv", index=False)
        pbar.update(1)

    print("=== FIN ===")

if __name__ == "__main__":
    main()

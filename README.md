# Análisis de Movimiento en Parque de Diversiones

Este proyecto analiza el movimiento y flujo de visitantes en un parque de diversiones mediante herramientas de Python y genera datos procesados para visualización en Power BI.

---

## Estructura del Proyecto

```
AnálisisParque/
├── data/                # Carpeta que contiene los archivos CSV (entrada y resultados)
├── modules/             # Módulos Python para análisis geométrico, optimización y estadística
├── reports/             # Archivos generados como Power BI y configuraciones
├── main.py              # Archivo principal para ejecutar los análisis
├── config.py            # Configuración del proyecto (ruta de datos)
├── requirements.txt     # Lista de dependencias necesarias
```

---

## Inicialización del Proyecto

### **Requisitos Previos**
- **Python**: Se recomienda instalar Python 3.9 o superior.
- **Bibliotecas necesarias**: Listadas en `requirements.txt`.
- **Entorno de desarrollo**: Recomendado PyCharm, pero también compatible con otros IDEs (como Anaconda, VSCode, Visual Studio).

### **Instalación de Dependencias**
Ejecuta el siguiente comando para instalar las dependencias:
```bash
pip install -r requirements.txt
```

---

## Configuración de Git y Subida al Repositorio

### **Inicializar y Vincular el Repositorio**
1. Clona el repositorio desde GitHub:
   ```bash
   git clone https://github.com/Andoresu23c/parque_analisis.git
   ```
2. Ingresa al directorio del proyecto:
   ```bash
   cd parque_analisis
   ```
3. Si ya tienes un proyecto local que deseas subir, configura el remoto:
   ```bash
   git remote add origin https://github.com/Andoresu23c/parque_analisis.git
   ```

### **Realizar el Commit Inicial**
1. Asegúrate de que todos los archivos están en el área de trabajo:
   ```bash
   git add .
   ```
2. Crea un commit con un mensaje descriptivo:
   ```bash
   git commit -m "Initial commit: Proyecto de análisis del parque"
   ```

### **Subir el Proyecto al Repositorio Remoto**
Si el remoto contiene cambios previos (como un README), puedes:

#### Opción 1: Combinar Cambios Remotos y Locales
1. Trae los cambios del remoto:
   ```bash
   git pull origin main --allow-unrelated-histories
   ```
2. Resuelve cualquier conflicto y realiza un commit adicional si es necesario:
   ```bash
   git add .
   git commit -m "Merge remoto y local"
   ```
3. Sube los cambios:
   ```bash
   git push origin main
   ```

#### Opción 2: Sobrescribir el Repositorio Remoto
Si deseas sobrescribir el contenido remoto completamente:
```bash
git push -f origin main
```
**Nota**: Esto eliminará el historial remoto.

---

## Ejecución del Proyecto

### **Con PyCharm (Recomendado)**
1. Abre el proyecto en PyCharm.
2. Configura el intérprete de Python.
3. Ejecuta `main.py` desde PyCharm.

### **Sin PyCharm (Otros IDEs o Terminal)**
1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el proyecto:
   ```bash
   python main.py
   ```

### **En macOS con Anaconda y Visual Studio**
1. **Instalar Anaconda:** Descarga e instala Anaconda desde [https://www.anaconda.com](https://www.anaconda.com).
2. **Crear un entorno en Anaconda:**
   ```bash
   conda create --name parque_env python=3.9
   conda activate parque_env
   ```
3. **Abrir Visual Studio:**
   - Abre Visual Studio y selecciona "Abrir un proyecto o solución".
   - Navega hasta el directorio del proyecto y ábrelo.
4. **Configurar el intérprete de Python en Visual Studio:**
   - Ve a las configuraciones del proyecto.
   - Selecciona el entorno de Python correspondiente (`parque_env`).
5. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Ejecutar el proyecto:**
   - En Visual Studio, selecciona `main.py` como archivo principal.
   - Ejecuta el proyecto desde la interfaz de Visual Studio.

### **Consideraciones para Anaconda**
Si utilizas Anaconda:
1. Crea un entorno compatible:
   ```bash
   conda create --name parque_env python=3.9
   conda activate parque_env
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el proyecto con:
   ```bash
   python main.py
   ```

---

## Resultados y Visualización

### **Generación de Datos**
- `main.py` generará los siguientes archivos CSV en la carpeta `data/`:
  - `analisis_geometrico.csv`
  - `optimizacion_funciones.csv`
  - `analisis_estadistico.csv`

### **Uso con Power BI**
1. Abre Power BI Desktop.
2. Importa los archivos CSV desde la carpeta `data/`.
3. Diseña visualizaciones basándote en las métricas generadas.
4. Guarda el archivo de Power BI en `reports/`.

---

## Manejo de Errores Comunes

### Error: `ModuleNotFoundError`
- **Causa**: No se instalaron las dependencias correctamente.
- **Solución**: Activa el entorno virtual y ejecuta:
  ```bash
  pip install -r requirements.txt
  ```

### Error: `FileNotFoundError`
- **Causa**: Falta el archivo `parque_datos.csv` en la carpeta `data/`.
- **Solución**: Asegúrate de que el archivo esté en la ubicación correcta.

### Error: `Python version mismatch`
- **Causa**: Versión incompatible de Python.
- **Solución**: Usa Python 3.9 o superior.

---
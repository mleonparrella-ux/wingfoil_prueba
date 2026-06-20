# wingfoil\_prueba

1. **Qué problema, experiencia o funcionalidad quiere desarrollar el grupo:**
Sistema para registrar sesiones de wingfoil y recibir recomendaciones de equipo basadas en el historial personal del deportista. El programa aprende de las sesiones pasadas y sugiere qué equipo usar según las condiciones del día.
2. **Quién sería el usuario del programa:**
Deportistas de wingfoil de cualquier nivel que quieran llevar un registro de sus sesiones y recibir recomendaciones personalizadas basadas en su experiencia propia.
3. **Qué podrá hacer el usuario al interactuar con el sistema:**
.Registrar cada sesión con: fecha, duración, ubicación, velocidad del viento, dirección del viento, equipo usado (wing, tabla, foil) y sensación (1-10)
.Ingresar las condiciones del día (viento, dirección, ubicación) y recibir una recomendación de equipo basada en sesiones similares del historial
4. **Qué información recibirá, procesará, generará o mostrará el programa:**
.Recibirá: datos de cada sesión ingresados por el usuario y condiciones del día para la recomendación.
.Procesará: búsqueda de sesiones similares en el historial, promedios de sensación por equipo.
.Mostrará: recomendación de equipo y un resumen de sesiones similares.
5. **Qué resultados, salidas o funcionalidades principales tendrá:**
.Registro histórico de sesiones guardado en EXCEL.
.Sistema de recomendación de equipo basado en condiciones similares del historial.
.Estadísticas de progreso a lo largo del tiempo.
.Consulta automática de viento y dirección según ubicación via API.
6. **Qué librerías y/o tecnologías usarán para el desarrollo del programa:**
.Python 
.PANDAS
.API de clima (OpenWeatherMap) para obtener velocidad y dirección del viento automáticamente según la ubicación.
7. **Cómo define "sesiones similares":**
.Misma ubicación
.Viento similar (±3 nudos)
.Misma dirección de viento
8. **Cómo calcula la recomendación:**
.Busca las 3 sesiones más similares del historial
.Recomienda el equipo con mayor sensación promedio en esas sesiones
9. **Qué pasa si hay poco historial:**
.Si hay menos de 3 sesiones similares, avisa al usuario y muestra las que hay.
.Si no hay ninguna, dice que no hay suficientes datos.
10. **Gráficos**:
.Sensación promedio por equipo.
.Ranking de wings por sensación.
11. **Validaciones:**

&#x20;  .Viento numérico positivo
.Sensación entre 1 y 10
.Duración positiva


## Uso de IA
Utilizamos Claude como herramienta de apoyo durante el desarrollo del proyecto. A continuación, los prompts más importantes:
1. Generación del dataset

"Creame un archivo Excel con más de 1000 sesiones de wing foil con columnas: Fecha, Ubicación, Duración (min), Vel. Viento (kn), Dir. Viento, Wing, Tabla, Foil y Sensación. Ubicaciones reales de Argentina, dirección del viento en español, viento entre 8 y 35 nudos, sensación entre 1 y 10."

2. Función de registro de sesión
"Tengo una función registrar_sesion en carga_datos.py que recibe un DataFrame y un diccionario con los datos de la nueva sesión. El problema es que cuando registro una sesión nueva se crea un Excel nuevo en vez de agregar al existente. ¿Qué está mal y cómo lo corrijo?"

3. Corrección de errores
"Tengo este error: TypeError: unsupported operand type(s) for -: 'str' and 'float' en recomendaciones.py al calcular la diferencia de viento. ¿Qué está pasando y cómo lo soluciono?"


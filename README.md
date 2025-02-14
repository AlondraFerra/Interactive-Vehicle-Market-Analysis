# [Link del proyecto en Render](https://proyecto5-fema.onrender.com)


# Análisis Interactivo del Mercado de Vehículos

## Contexto
En la compra y venta de vehículos, el kilometraje y el precio son factores determinantes para la toma de decisiones. Esta aplicación interactiva permite visualizar y analizar información clave sobre vehículos disponibles en el mercado, facilitando la identificación de patrones y tendencias. Su objetivo es ayudar a compradores y vendedores a tomar decisiones informadas basadas en datos.

## Herramientas Utilizadas
- **Python:** Para la manipulación y análisis de datos.
- **Pandas:** Para la limpieza y estructuración de la información.
- **Matplotlib y Seaborn:** Para la generación de visualizaciones estadísticas.
- **Plotly/Dash:** Para la creación de la aplicación interactiva.
- **Dataset:** Información de vehículos en venta con detalles como kilometraje, precio, año y tipo de combustible.

## Funcionalidades y Visualizaciones
La aplicación proporciona dos visualizaciones clave para el análisis del mercado automotriz:

**Histograma de Kilometraje**

- Muestra la distribución de los vehículos según el kilometraje registrado en su odómetro.
- Permite filtrar los datos según el tipo de combustible (gasolina, diésel, eléctrico, híbrido).
- Ayuda a identificar rangos de kilometraje más comunes en el mercado.

**Gráfico de Dispersión de Kilometraje y Precio**

- Representa la relación entre el kilometraje y el precio de los vehículos.
- Utiliza diferentes colores para distinguir los años de los vehículos anunciados.
- Facilita la detección de tendencias de depreciación y posibles valores atípicos.

## Análisis de Resultados
A partir de las visualizaciones generadas, se pueden extraer los siguientes hallazgos:

- **Distribución del Kilometraje:** La mayoría de los vehículos en venta se agrupan en ciertos rangos de kilometraje, lo que indica la oferta más común en el mercado.
- **Relación Kilometraje-Precio:** Se observa una tendencia clara de depreciación: los vehículos con mayor kilometraje suelen tener precios más bajos, aunque hay excepciones dependiendo de la marca y el modelo.
- **Año del Vehículo:** Los modelos más recientes presentan menor kilometraje y precios más altos, mientras que los modelos antiguos tienen una mayor dispersión en el precio.

## Conclusiones
Esta aplicación proporciona una herramienta útil para analizar el mercado de vehículos en función del kilometraje y el precio. Al permitir la exploración interactiva de los datos, ayuda a compradores y vendedores a entender mejor la oferta disponible y detectar patrones de depreciación. Además, la segmentación por tipo de combustible ofrece información valiosa sobre las preferencias del mercado.

En futuras versiones, se podrían incluir más filtros y métricas, como la marca y el modelo del vehículo, para hacer el análisis aún más completo.


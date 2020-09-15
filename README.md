![gpcover](https://user-images.githubusercontent.com/66042132/93179328-cd6cac00-f735-11ea-892d-f96dadbe8b31.png)

###**Proyecto- Top Free Games Google Play**

Para este proyecto se escogió el dataframe de Kaggle [Google Play Store Apps](https://www.kaggle.com/lava18/google-play-store-apps/notebooks), el cual está compuesto de información de todas las Apps de Google Play del año 2018 y en donde nos vamos a centrar en los Juegos gratis, los cuales son la 2da categoría mas descargada de la App, siendo la 1era categoría las Apps con temática de Familia, según el propio dataframe.

**Apis vs. Dataframe:**

Con la visión de enriquecer los ratings de dicho dataframe, se trabaja con la API de Google Play Top Free Games, actualizado.

**Ejecución del programa:**

Para ejecutar el programa, es necesario llamarlo desde la terminal de la siguiente manera: python3 main.py Y añadirle las flags con los argumentos a buscar:}
-r es rating,
-t es tipo de juego, el cual será Free por defecto, ya que son con los que trabajamos
-g el genero del juego:
    - Action
    - Strategy
    - Arcade
    - Puzzle
    - Casual
    - Racing
    - Board
    - Word
    - Sports
    - Card
    - Casino
    - Trivia
-c el tipo de contenido  que buscamos:
    - Everyone
    - Teen
    - Everyone +10
    - Mature +17 

**Metodología:**

Se importaron Todos los paquetes a necesitar como Pandas, Numpy,os, dotenv, json, requests, argparse y un paquete para poder expresar los gráficos llamado pyplot. Seguido de un primer contacto con los datos, viendo su forma, cantidad de elementos nulos que poseían sus columnas, cantidad de filas y elementos duplicados por columnas y filas. Posteriormente se realizó una limpieza del [dataframe](output/limpiezadf.py) y del dataframe extraído de la [API](output/limpiezaApi.py). Posteriormente se trabajo en un archivo main donde se correra el proyecto.

**Documentos encontrados:**
°Carpeta de Output: Con las gráficas producidas.
°Carpeta SRC: Con las funciones usadas para la realización de la actividad.
°Readme: Resumen de la actividad realizada

**Apredizaje:** 
Uso de API's con fucion a dataframes

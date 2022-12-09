#            PROYECTO INDIVIDUAL #1 : DATA ENGINEER 

<p align="center">
<img src="https://raw.githubusercontent.com/isaacpc94/PI01_DATA05/main/images/data%20engineer.jpg"  height=300><br>

# Descripción del proyecto:

- Construir una "API" para poder hacer consultas sobre las plataformas: amazon, disney, hulu y netflix.<br><br>

# Proceso ETL:
- 1: El proceso ETL se ejecuta en el archivo "ProyectoETL.ipynb". <br>

- 2: Los archivos "csv." en la carpeta "Datasets" son leidos y ejecutados por este archivo, luego son transformados y finalmente se genera archivos "csv." dentro de la carpeta "tables".<br><br>

# Base de datos:

- Los archivos "csv."  generados por el proceso ETL son ejecutados por el archivo "createdb.py" que genera una base de datos".<br><br>

# APP:

- El archivo "main.py" dentro de la carpeta "app" contiene todas las funciones que la aplicación necesita para realizar sus consultas  a la base de datos.<br><br>

# Instrucciones para ejecutar la API:

- 1: Clonar el repositorio https://github.com/isaacpc94/PI01_DATA05.git.<br>

- 2: Crear la base de datos ejecutando el archivo "createdb.py".<br>

- 3: Crear la imagen usando el archivo Dockerfile con la siguiente instrucción:<br>          "docker build -t apifastisaac" .<br>

- 4: Crear el contenedor con la siguiente instrucción: <br>
"docker run -d --name contenedorisaac -p 80:80 apifastisaac".<br>

- 5: Iniciar el contenedor en caso este apagado con la siguiente instrucción:<br>
    "docker start -a contenedorisaac".

- 6: Abrir navegador en "hostname:80".<br><br>

# Como usar la API:
- get_max_duration: <br>
    Parametros: Año, plataforma y tipo de tiempo("min" o "season")<br>
    Resultado: Pelicula o serie con mayor duración y cuanto es esta duración.<br>

- get_count_plataform: <br>
        Parametros: Plataforma.<br>
        Resultado: Cantidad de películas y series de la plataforma seleccionada.<br>

- get_listedin: <br>
    Parámetros: Género de película o serie.<br>
    Resultado: Plataforma con mas contenido del género seleccionado y su cantidad.<br>

- get_actor: <br>
    Parámetros: actor/actriz<br>
    Resultado: Plataforma en la que mas se encuentra el actor/actriz escogido y su cantidad.<br><br>



<p align="center">
<img src="https://raw.githubusercontent.com/isaacpc94/PI01_DATA05/923fc381c7d59a5732ab1a726d081fdc28de1e83/images/API.jpg"  height=300>




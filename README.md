# PI01_DATA05
PI Data Engineer Cohorte 05

Pasos

ETL:
    . El proceso ETL se ejecuta en el archivo "Proyecto.ipynb" 
    . Los csv en la carpeta Datasets son leidos por este archivo, luego son transformados y finalmente se genera csv dentro de la carpeta "tables"

SQL:
    .Los csv generados por el proceso ETL son cargados a MySQL Workbench y se genera una base de datos, en donde se pueden hacer consultas.

Funciones de consulta:
    .Las funciones de consulta se encuentran en el archivo "funcionessql.py"

API:
    .Se levanta el servidor uvicron desde el terminal.
    .EL proceso APIFAST se encuentra en el archivo "main.py" esta ejecuta funciones  de consulta que seran 
     .Una vez ejecutado este nos proporcionara un link que debe mostrarse como la siguinte imagen.
    .![asd](images\API.jpg)
    


# PI01_DATA05
PI Data Engineer Cohorte 05

Pasos

ETL:
    . El proceso ETL se ejecuta en el archivo "Proyecto.ipynb" <br>
    . Los csv en la carpeta Datasets son leidos por este archivo, luego son transformados y finalmente se genera csv dentro de la carpeta "tables"<br>

SQL:
    .Los csv generados por el proceso ETL son cargados a MySQL Workbench y se genera una base de datos, en donde se pueden hacer consultas.

Funciones de consulta:
    .Las funciones de consulta se encuentran en el archivo "funcionessql.py"

## API
adawdafafa:

- 1:Se levanta el servidor uvicron desde el terminal.<br>
- 2:EL proceso APIFAST se encuentra en el archivo "main.py" esta ejecuta funciones  de consulta que seran <br>
-Una vez ejecutado este nos proporcionara un link que debe mostrarse como la siguinte imagen.<br>
-![](https://raw.githubusercontent.com/isaacpc94/PI01_DATA05/923fc381c7d59a5732ab1a726d081fdc28de1e83/images/API.jpg)

<p align="center">
<img src="https://raw.githubusercontent.com/isaacpc94/PI01_DATA05/923fc381c7d59a5732ab1a726d081fdc28de1e83/images/API.jpg"  height=300>

    
## Funciones en SQL
Como vimos en el apartado anterior, para construir KPI es importante relacionar distintas variables y obtener conclusiones a partir de los calculos que realizamos. Comencemos ahora con un primer acercamiento en SQL.

Al igual que en Excel, algunos lenguajues de programación y software estadísticos, hay que tener en cuenta lo siguiente a la hora de utilizar una función:

- Acción: es poco probable que conozcas todas las funciones que forman parte de SQL, por lo es importante al momento de buscar una función o funcionalidad, entender que tipo de acción u operación deseamos realizar.<br>
Ej: Quiero buscar una palabra específica en un campo y saber cuantas veces aparece (LIKE y COUNT). <br>
- Sintaxis: las fucniones poseen un nombre que esta dado por una palabra reservada y una forma específica de invocarla. Si ese nombre no se escribe de manera correcta, se iuncurre en un error de sintaxis.<br>


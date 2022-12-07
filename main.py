from fastapi import FastAPI
from funcionessql import maxduration as max
from funcionessql import cantpys as cant
from funcionessql import genero as gen
from funcionessql import actor as act
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worldado"}

@app.get("/get_max_duration({anio},{plat},{minoseason})")  
async def maxduration(anio:int,plat:str,minoseason:str):
    if minoseason=="min":
        return {"La Pelicula con mas duración es ": max(anio,plat,minoseason)[0][0],
                "con una duración de" : max(anio,plat,minoseason)[0][4]}
    elif minoseason=="season":
        return {"La Serie con mas duración es ":max(anio,plat,minoseason)[0][0],
                "con una duración de" : max(anio,plat,minoseason)[0][4]}
    else:
        return {"Inserte sin o season en el tercer parametro"}

@app.get("/get_count_plataform({plat})") 
async def cantidadp(plat:str):
    return {"En la plataforma" : cant(plat)[0][0],
            "la cantidad de peliculas es" : cant(plat)[0][2],
            "la cantidad de series es" : cant(plat)[1][2]}

@app.get("/get_listedin({genero})") 
async def cantidadg(genero:str):
    return {"La Plataforma con mas cantidad de este genero es" : gen(genero)[0][0],
            "con una cantidad de" : gen(genero)[0][2]}

@app.get("/get_actor({plat},{anio})") 
async def actor(plat:str,anio:int):
    return {"El actor que mas se repite en esta plataforma es" : act(plat,anio)[0][1],
            "cuya cantidad es" : act(plat,anio)[0][4]}






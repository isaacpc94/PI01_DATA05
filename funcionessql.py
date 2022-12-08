import pandas as pd
import numpy as np
from fastapi import FastAPI
import json
import pymysql


def conectar_a_base_de_datos() :
    conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    db= 'video',
    port=3307
    )
    return conexion.cursor()


#1 Funcion que recibe año y plataforma y tipo de tiempo y retorna la pelicula o serie y su duracion maxima.
def maxduration(anio,plataforma,time):
    cursor=conectar_a_base_de_datos()
    a=[]
    anio=str(anio)
    if time=="min":
        query="select d.title,d.release_year,d.Plataforma,d.type,d.duration,convert(SUBSTRING_INDEX(d.duration,' ', 1), UNSIGNED INTEGER) AS durnum from \
        (select a.IdPlataforma,a.Plataforma,b.duration,c.release_year,c.type,c.title from\
        idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)\
        join video c on (binary b.IdVideo=binary c.IdVideo)\
        ) d where d.type='Movie' and d.Plataforma='"+plataforma+"' and d.release_year="+anio+ \
        " order by 6 desc \
        limit 1"
        cursor.execute(query)
    elif time=="season":
        query="select d.title,d.release_year,d.Plataforma,d.type,d.duration,convert(SUBSTRING_INDEX(d.duration,' ', 1), UNSIGNED INTEGER) AS durnum from \
        (select a.IdPlataforma,a.Plataforma,b.duration,c.release_year,c.type,c.title from\
        idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)\
        join video c on (binary b.IdVideo=binary c.IdVideo)\
        ) d where d.type='TV Show' and d.Plataforma='"+plataforma+"' and d.release_year="+anio+ \
        " order by 6 desc \
        limit 1"
        cursor.execute(query)
    else:
        return "Inserte [min] o [season] en el tercer parametro"

    for dato in cursor:
        a.append(dato)
    
    return a
    


#2 Funcion que retorna  cantidad de Pelicuals y series de la plataforma escogida
def cantpys(plataforma):
    cursor=conectar_a_base_de_datos()
    a=[]
    cursor.execute("select a.Plataforma,c.type,count(*) from \
    idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma) \
    join video c on (binary b.IdVideo=binary c.IdVideo) \
    where a.Plataforma='"+plataforma+"' \
    group by 2 order by 2")
    for dato in cursor:
        a.append(dato)
    
    return a
    

#3 Funcion que retorna la Plataforma con la mayor cantidad del genero insertado
def genero(genero):
    cursor=conectar_a_base_de_datos()
    a=[]
    query="select a.Plataforma,c.listed_in,count(*) from \
    idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma) \
    join (select * from listed  \
    where listed_in = '"+genero+"') c on (b.IdPlataforma= c.IdPlataforma and (binary b.IdVideo= binary c.IdVideo) ) \
    group by 1 \
    order by 3 desc \
    limit 1"
    cursor.execute(query)
    for dato in cursor:
        a.append(dato)
    
    return a
    

#4 Funcion que retorna el actor y la frecuencia con que se repite para el año y plataforma seleccionados
def actor(plataforma,anio):
    cursor=conectar_a_base_de_datos()
    a=[]
    anio=str(anio)
    query="select a.Plataforma,d.cast,b.IdVideo,c.release_year,count(*) as cantidad from \
    idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma) \
    join video c on (binary b.IdVideo=binary c.IdVideo) \
    join cast d on (binary c.IdVideo=binary d.IdVideo) \
    where a.Plataforma='"+plataforma+"' and c.release_year="+anio+" \
    group by d.cast \
    having cast !='' \
    order by 5 desc \
    limit 1"
    cursor.execute(query)
    for dato in cursor:
        a.append(dato)
    
    return a
    
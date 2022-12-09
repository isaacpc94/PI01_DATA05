import pandas as pd
import numpy as np
from fastapi import FastAPI
import json
import pymysql

conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    port=3307
    )
cursor=conexion.cursor()
#crea la database
cursor.execute("create database if not EXISTS video2")
cursor.close()

conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    db= 'video2',
    port=3307
    )

    
cursor=conexion.cursor()
#crea todas las tablas
with open('createdb/video_routines.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()

cursor=conexion.cursor()
with open('createdb/video_idplataformap.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()

cursor=conexion.cursor()
with open('createdb/video_cast.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()

cursor=conexion.cursor()
with open('createdb/video_listed.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()

cursor=conexion.cursor()
with open('createdb/video_plataforma.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()

cursor=conexion.cursor()
with open('createdb/video_video.sql',encoding="utf-8") as myfile:
  data = myfile.read()
  data=data.split(";")
  for i in data:
    cursor.execute(i)
cursor.close()


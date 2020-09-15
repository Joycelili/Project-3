import os
from dotenv import load_dotenv
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime 
import search as sea
import argparse



def cargaDataSet():
    """llamada al dataset"""
    global data
    data = pd.read_csv("output/limpiezadf.csv")
    return data

def requestRating(r):
    """  rating de las apps  """
    return scores[f'{r}']

def search_name(n):
"""Datos la app elegida"""
    return df[df['App']==f'{n}'][['App','Content Rating','Rating','Genre']]

def search_genre(g):
"""Llamado por genero de juego"""
    return df[df['Genre']==f'{g}'][['App','Content Rating','Rating','Genre']]

def search_content(c):
"""Busca por  tipo de contenido  """
    return df[df['Content Rating']==f'{c}'][['App','Content Rating','Rating','Genre']]

def typegenre(g):
    genre =["Action", "Strategy", "Arcade", "Puzzle", "Casual", "Racing", "Board", "Word", "Sports", "Card", "Casino","Trivia"]
    if g not in genre:
        raise argparse.ArgumentTypeError(f"No hay de este género {g}")
    else:
        print(genre(g))
        
def typecontent(c):
    content=["Everyone", "Teen ", "Everyone +10", "Mature +17"]
    if x not in content:
        raise argparse.ArgumentTypeError(f"No hay de la clificicación que buscas {c}")
    else:
        print(content(c))

def mean_info(x):
    data = pd.read_csv('output/limpiezadf.csv')
    m = data[x].mean()
    return print('The mean is:', m)
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
    global data
    data = pd.read_csv("output/limpiezadf.csv")
    return data

parser = argparse.ArgumentParser(description = "Accede a información sobre tu google app de los juegos preferidos")
parser.add_argument("-r" ,dest="rating",type=float,help="Introduce el rating mínimo deseado(valor entre 0-9)",default=0)
parser.add_argument("-n",dest="name",type=str,help="Escribe el título del Juego del que quieras obtener información (Entre comillas 'titulo')", default='None')
parser.add_argument("-g" ,dest="genre",type=str,help="Introduce el género que desea:\n - Action\n - Strategy\n - Arcade\n -  Puzzle\n - Casual\n - Racing\n -  Board\n - Word\n - Sports\n - Card\n - Casino\n - Trivia\n",default='None')
parser.add_argument("-c",dest="content_rating",type=str,help="Introduce el tipo de contenido  que deseas:\n - Everyone\n - Teen\n - Everyone +10\n - Mature +17 \n", default='None')
args = parser.parse_args()
print(args)
     
def main(rating,name,genre,content_rating):
    args = parse()
    rating = args.rating
    name = args.name
    genre = args.genre
    content_rating = args.content_rating
    if args.rating != 0:
        print(sea.requestRating())
    if args.name != None:
        print(sea.requestTpe()) 
    if args.typegenre != None:
        print(sea.requestGenre())
    if args.typecontent != None:
        print(sea.requestContRat())

sea.statistical_info('Rating')

if __name__ == "__main__":
        main()
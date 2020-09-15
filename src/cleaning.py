import os
from dotenv import load_dotenv
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime 
import argparse


def fil_na(x):
    """rellena todos los NaN con 0"""
    x= x.fillna(0, inplace=True)
    return x

def sortValues(df):
    """Organiza el df según el rating de mayor a menor"""
    df2= df.sort_values(by="rating",ascending=False)
    return df2

def eli_dupli_col(data,nombre):
    """Elimina los duplicados de la columna que seleccionemos.
    Donde data es nombre de dataframe y nombre será el nombre de la comumna"""

    drop_dupli = data.drop_duplicates(subset=[f"{nombre}"], keep='last').reset_index(drop=True)
    return drop_dupli







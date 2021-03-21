# -*- coding: utf-8 -*-

import os
import multiprocessing as mp
import arcpy
import pandas as pd

import time
shp_path = "D:/Users/Document/Tencent Files/279871734/FileRecv/世界国家/世界国家.shp"
csv_path = "D:/research/covid-19/covid-19/data/countries-aggregated.csv"

DATA_path = "D:/research/covid-19/covid-19/data_cou.csv"
SHP_path = "D:/research/covid-19/covid-19/shp_cou.csv"
def check():

def translate():
    with open(DATA_path, "r") as f:

if __name__ == '__main__':
    data = pd.read_csv(csv_path)
    months = []
    for i in 9:
        months.append("2020/" + str(i + 1) + "/")
    for i in 3:
        months.append("2020/" + str(i + 10))
        months.append("2021/" + str(i + 1) + "/")
    cursor = arcpy.UpdateCursor(shp_path,"","","","id_fine_wh A")
    print ("start...")
    for row in cursor:
        The_Line = data[data.LID == row.id_fine_wh]
        The_Index = The_Line.index
        PAFRAC = The_Line.loc[The_Index, ' PAFRAC']
        row.PAFRAC = float(PAFRAC)
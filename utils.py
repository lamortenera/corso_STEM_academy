# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:26:20 2019

@author: ale
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict

OWM_KEY = "incolla_qui_la_tua_chiave"
DB_PATH = os.path.join(os.path.dirname(__file__), "database.csv")
CHART_PATH = os.path.join(os.path.dirname(__file__), "static", "chart.png")
CITIES = ["Padova", "Milano", "Roma", "Firenze", "Napoli"]

def data_to_chart(data):
    data = sorted(data, key=lambda row: row["datetime"])
    lines = defaultdict(lambda : {"x": [], "y": []})
    for row in data:
        line = lines[row["city"]]
        line["x"].append(row["datetime"])
        line["y"].append(row["temperature"])
    for city, line in lines.items():
        plt.plot(line["x"], line["y"], label=city)
    plt.xlabel("data")
    plt.ylabel("temperatura")
    plt.title("temperatura per città")
    plt.legend()
    plt.gcf().autofmt_xdate()
    with open(CHART_PATH, 'w') as out_stream:
        plt.savefig(out_stream, format="png")
    plt.clf()

def write_data():
    print("Non implementato.")

def read_data():
    print("Non implementato.")
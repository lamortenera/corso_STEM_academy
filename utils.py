# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:26:20 2019

@author: ale
"""
import datetime
import os
import matplotlib
import urllib.request
import json
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict

OWM_KEY = "c4dd883dc03666b90ca628bf95e0bd58"
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
    plt.savefig(CHART_PATH, format="png")
    plt.clf()

def data_to_json(data):
    data = sorted(data, key=lambda row: row["datetime"])
    charts = {}
    for row in data:
        city = row["city"]
        if city not in charts:
            charts[city] = {"x": [], "y": [], "mode": "lines", "name": city}
        chart = charts[city]
        chart["x"].append(str(row["datetime"]))
        chart["y"].append(row["temperature"])
    chart_list = list(charts.values())
    return json.dumps(chart_list)
    
    
def get_temperature(city):
    url_base = "https://api.openweathermap.org/data/2.5/weather"
    url = url_base + "?appid={}&q={}".format(OWM_KEY, city)
    response_bytes = urllib.request.urlopen(url).read()
    d = json.loads(response_bytes.decode("utf8"))
    return d["main"]["temp"] - 273.15

def datetime_to_str(dt):
    return "{}_{}_{}_{}_{}_{}".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

def str_to_datetime(dt_str):
    return datetime.datetime(*[int(tok) for tok in dt_str.split('_')])

def format_row(row_dict):
    return "{},{},{}".format(
        datetime_to_str(row_dict["datetime"]), row_dict["city"], row_dict["temperature"])

def parse_row(row_csv):
    args = row_csv.split(",")
    dt = str_to_datetime(args[0])
    city = args[1]
    temperature = float(args[2])
    return {"datetime": dt, "city": city, "temperature": temperature}
    
def write_data():
    dt = datetime.datetime.now()
    newline = "\n"
    with open(DB_PATH, 'a') as out_stream:
        for city in CITIES:
            temperature = get_temperature(city)
            data_row = {"datetime": dt, "city": city, "temperature": temperature}
            csv_row = format_row(data_row)
            out_stream.write(csv_row + newline)
        
def read_data():
    data = []
    newline = "\n"
    with open(DB_PATH, 'r') as in_stream:
        for line in in_stream:
            csv_row = line.strip(newline)
            data_row = parse_row(csv_row)
            data.append(data_row)
    return data

def get_table_content(data):
    content = ""
    row_pattern = "<tr><td>{}</td><td>{}</td><td>{:.2f}</td></tr>"
    for row in data:
        content += row_pattern.format(row["datetime"], row["city"], row["temperature"])
    return content

def get_form_content(allowed_cities):
    content = ""
    pattern = "<input type='checkbox' name='filter_value' value='{}' {}>{}<br>"
    for city in CITIES:
        checked = ""
        if not allowed_cities or city in allowed_cities:
            checked = "checked"
        content += pattern.format(city, checked, city)
    return content

def filter_data(data, allowed_cities):
    new_data = []
    for row in data:
        if row["city"] in allowed_cities:
            new_data.append(row)
    return new_data

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:26:20 2019

@author: ale
"""
import os

OWM_KEY = 'incolla_qui_la_tua_chiave'
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.csv')
CITIES = ["Padova", "Milano", "Roma", "Firenze", "Napoli"]

def write_data():
	print("Non implementato.", end="")
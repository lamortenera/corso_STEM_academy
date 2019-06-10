# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:30:59 2019

Due cose importanti:
* Come si importa una funzione da un file diverso
* Come si scrive la funzione `main`
* Come si scrive un ciclo infinito

@author: ale
"""
import time
import ctypes
from contextlib import contextmanager
from utils import write_data

# Questo codice disabilita la modalita' sleep
# del computer finche' il codice e' in esecuzione.
@contextmanager
def nosleep_context():
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001    
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED)    
    print("Modalita' sleep disabilitata") 
    try:
        yield
    finally:
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        print("Modalita' sleep riabilitata")
        
if __name__ == "__main__":
    with nosleep_context():
        while True:
            print("Rilevamento dati meteo... ", end="")    
            write_data()
            print(" Fine. CTRL+C per interrompere")
            time.sleep(60*5)
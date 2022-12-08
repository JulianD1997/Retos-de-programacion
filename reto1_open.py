"""
Nivel: Inicial
Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls). """

import pandas as pd
import re

excel = pd.read_excel('D:/programacion/python/retos_moure/Lista Mails.xls')
correos = excel['Unnamed: 8']
for correo in correos:
    if(re.match(r'\S+;',correo)):
        print(correo.split(';')[0])
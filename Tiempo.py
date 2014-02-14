# coding: utf-8
import requests
import json


des = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla"}

print 
"""
1. Sevilla
2. Malaga
3. Cadiz
4. Cordoba
5. Huelva
6. Granada
7. Jaen
8. Almeria
"""
peticionn = raw_input("¿De qué ciudad quieres saber la temperatura actual?: ")

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peti]})

dicci = json.loads(respuesta.text)

temperatura = dicci["main"]["temp"] 

tempreal = temperatura - 273

print "la temperatura actual de %s es de %s C" % (ciudades(peticion),tempreal)

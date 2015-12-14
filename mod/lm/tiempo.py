#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
response = urllib2.urlopen('http://openweathermap.org/city/2518794')
lineas=response.readlines()
lineas=lineas[968:989]
print "Temperatura:"
inicio=lineas[2].find("png")+6
fin=lineas[2].find("C</")+1
print lineas[2][inicio:fin]
print "Presión:"
print lineas[16].split("<td>")[2].split("<")[0]
print "Humedad"
fin=lineas[19].find("%")+1
inicio=lineas[19].find("</td><td>")+len("</td><td>")
print lineas[19][inicio:fin]

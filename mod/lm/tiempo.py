#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
response = urllib2.urlopen('http://openweathermap.org/city/2518794')
lineas=response.readlines()
lineas=lineas[968:987]
print "Temperatura:"
inicio=lineas[0].find("png")+6
fin=lineas[0].find("C</")+1
print lineas[0][inicio:fin]
print "Presión:"
print lineas[14].split("<td>")[2].split("<")[0]
print "Humedad"
fin=lineas[17].find("%")+1
inicio=lineas[17].find("</td><td>")+len("</td><td>")
print lineas[17][inicio:fin]

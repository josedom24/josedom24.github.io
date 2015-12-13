#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
nombre=raw_input("Usuario de twitter:")
error=False
try:
	response = urllib2.urlopen('https://twitter.com/'+nombre)
except urllib2.HTTPError:
	print "Usuario no encontrado"
	error=True
if not error:
	lineas=response.readlines()
	print lineas[935].split(">")[1].split("<")[0]
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

USUARIOS=12
PS_INI=8006
P_INI=8081

puertos=[]
for u in xrange(0,USUARIOS):
	puertos.append((P_INI,PS_INI))
	P_INI=P_INI+1
	PS_INI=PS_INI+1

print puertos
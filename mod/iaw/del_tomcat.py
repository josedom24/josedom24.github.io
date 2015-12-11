#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

USUARIOS=2
DIR="/home/"
DIR2="/opt/tomcat/"
puertos=[]
for u in xrange(0,USUARIOS):

        os.system("userdel %s"%("tomcat-"+str(u+1)))
        os.system("delgroup %s"%("tomcat-"+str(u+1)))
        os.system("rm -r %s"%(DIR2+"tomcat-"+str(u+1)))
        os.system("rm -r %s"%(DIR+"tomcat-"+str(u+1)))


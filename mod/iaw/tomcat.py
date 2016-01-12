#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

USUARIOS=12
PS_INI=8006
P_INI=8081
DIR="/home/"
DIR2="/opt/tomcat/"
puertos=[]
for u in xrange(0,USUARIOS):
	puertos.append((P_INI,PS_INI))
	P_INI=P_INI+1
	PS_INI=PS_INI+1

for u in xrange(0,USUARIOS):
	os.system("useradd -d %s -m -s /bin/bash %s"%(DIR+"tomcat-"+str(u+1),"tomcat-"+str(u+1)))
	os.system("chown %s:%s %s"%("tomcat-"+str(u+1),"tomcat-"+str(u+1),DIR+"tomcat-"+str(u+1)))		
	os.system("echo %s:asdasd | chpasswd" %("tomcat-"+str(u+1)))
	os.system("usermod -g tomcat7 tomcat-%s" % str(u+1))


cont=1
for puerto,puerto_sh in puertos:
	os.system("tomcat7-instance-create -p %i -c %i -w %s %s" % (puerto,puerto_sh,"SHUTDOWN"+str(cont),DIR2+"tomcat-"+str(cont)))
	os.system("chown %s:%s %s"%("tomcat-"+str(cont),"tomcat-"+str(cont),DIR2+"tomcat-"+str(cont)))			
	os.system("ln -s %s %s/tomcat"%(DIR2+"tomcat-"+str(cont),DIR+"tomcat-"+str(cont)))
	os.system("chown -h %s:%s %s/tomcat"%("tomcat-"+str(cont),"tomcat-"+str(cont),DIR+"tomcat-"+str(cont)))	
	os.system("chown -R %s:%s %s/tomcat/*"%("tomcat-"+str(cont),"tomcat-"+str(cont),DIR+"tomcat-"+str(cont)))	
	cont=cont+1



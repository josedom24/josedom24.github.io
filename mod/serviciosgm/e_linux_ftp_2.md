---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de proFTPd para crear ftp anónimo

Queremos crear un ftp anónimo que acceda al directorio /var/ftp, para ello hay que seguir los siguientes pasos:

1) Lo primero que tenemos que hacer es crear el directorio y darle el propietario adecuado:


        mkdir /var/ftp
        chown proftpd:nogroup /var/ftp


2) Podemos tener los  dos mecanismos simultáneamente: autentificación y anónimo. Si no queremos que puedan acceder los usuario de manera autentificada, tengo que poner el fichero de configuración (/etc/proftpd/proftpd.conf):

        <Limit LOGIN>
          DenyAll 
        </Limit>

3) Podemos crear el directorio de acceso anónimo de sólo lectura o lectura escritura, para ello descomentamos las lineas del fichero de configuración que empiezan por: Anonymous..., indicando el directorio donde se va a acceder:

        <Anonymous ~ftp>
          User                                ftp
          Group                               nogroup
          ...
	</Anonymous>


<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1. Realiza las configuraciones necesarias para configurar un ftp anónimo.
2. Accede desde el cliente ftp desde linux y windows
</div>
[Volver](index)

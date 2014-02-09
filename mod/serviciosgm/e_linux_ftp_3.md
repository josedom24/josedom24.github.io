---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Gestión de páginas web mediante ftp

Siguiendo la funcionalidad del servidor FTP vista en la práctica anterior, podemos hacer uso de ella para que un usuario pueda acceder al directorio particular de un sitio web y pueda modificar los ficheros de dicho sitio.

Para ello vamos a realizar los siguientes pasos:

1) Vamos a crear dos sitios webs virtuales en el servidor apache2 que se llamen web1.iesgn.com y web2.iesgn.com, los directorios particuales de dichos sitios van a ser los siguientes:

* web1.iesgn.com -> /home/usuario1/web
* web2.iesgn.com -> /home/usuario2/web

2) Hemos creados los usuarios: usuario1 y usuario2. ahora tenemos que modificar la confuiguración del servidor proftpd para que cuando accedamos con usuario1 acceda a la carpeta /home/usuario1/web y cuando acceda usuario2 entre en /home/usuario2/web

3) Modifica el servidor DNS para que web1.iesgn.com y web2.iesgn.com apunte a la ip del servidor.

4) Entra en el ftp y sube a cada sitio la página web que podéis descargar desde la plataforma ([web1.zip](files/web1.zip) y [web2.zip](files/web2.zip)).

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1. Modifica de forma adecuada el servidor DNS para poder realizar la práctica.
2. Accede con un cliente ftp con el usuario usuario1 y usuario2, y sube la página a cada espacio.
3. Comprueba el acceso a las páginas web.
</div>
[Volver](index)

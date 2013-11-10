---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Gestión de páginas web mediante aceeso FTP
Siguiendo la funcionalidad del servidor FTP vista en la práctica anterior, podemos hacer uso de ella para que un usuario pueda acceder al directorio particular de un sitio web y pueda modificar los ficheros de dicho sitio.

Para ello vamos a realizar los siguientes pasos:

1) Vamos a crear dos sitios webs virtuales en el servidor IIS que se llamen web1.iesgn.com y web2.iesgn.com, los directorios particuales de dichos sitios van a ser los siguientes:

* web1.iesgn.com -> c:/usuarios/LocalUser/web1
* web2.iesgn.com -> c:/usuarios/LocalUser/web2

2) Si te fijas hemos hecho coincidir los directorios particulares de los sitios webs con los directoios particulares de los sitios FTP para dos usuarios web1 y web2. Con lo que sólo tendremos que crear esos dos usuarios web1 y web2.

3) Modifica el servidor DNS para que web1.iesgn.com y web2.iesgn.com apunte a la ip del servidor.

4) Entra en el ftp y sube a cada sitio la página web que podéis descargar desde la plataforma ([web1.zip](files/web1.zip) y [web2.zip](files/web2.zip)).

[Volver](index)

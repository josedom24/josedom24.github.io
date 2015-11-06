---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de un servidor FTP con acceso autentificado

Antes de comenzar esta práctica debes detener el sitio FTP que configuraste en la páctica anterior y hacer uno nuevo.

El objetivo de esta práctica es que los usuarios locales del equipo puedan tener un directorio particular en el servidor FTP.

Para ello sigue los siguiente pasos:

1) Crea un nuevo sitio FTP con la opción de aislamiento de usuario indicada *"Directorio físico de nombre de usuario"*, de lectura y escritura. En un primer momento no permita los accesos anónimos. El directorio paricular será c:/ftp/usuarios.

2) Crea dos usuarios locales: Jose y Maria.

3) Para que los dos usuarios puedan acceder a un directorio propio en el servidor FTP tendrás que crear un directoio LocalUser dentro del directorio particular, y dentro de este un directorio con el nombre de cada usuario. Es decir debes crear los siguientes directorios:

* c:/ftp/usuarios/LocalUser/Jose
* c:/ftp/usuarios/LocalUser/Maria

Coloca dentro de ellos algunos ficheros para comprobar su funcionamiento.

4) Accede a ftp.iesgn.com, comprueba que tienes que autentificarte y comprueba el acceso con los dos usuarios.

5) Para que puedan acceder usuarios anónimos debemos habiliatar la autentificación anónima y en las Reglas de autorización debemos añadir la opción de usuarios anónimos. Los usarios anónimos accederan a una carpeta llamada: c:/ftp/usuarios/LocalUser/Public


[Volver](index)

---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Autentificación básica

El servidor web Apache puede acompañarse de distintos módulos para proporcionar diferentes modelos de autenticación.
La primera forma que veremos es la más simple. Usamos para ello el módulo de autenticación básica que viene instalada “de serie” con cualquier Apache: [mod_auth_basic](http://httpd.apache.org/docs/2.2/es/mod/mod_auth_basic.html). La configuración que tenemos que añadir en el fichero de definición del Virtual Host a proteger podría ser algo así:

        <Directory "/var/www/miweb/privado">
         Order deny,allow
         AuthUserFile "/etc/apache2/claves/passwd.txt"
         AuthName "Palabra de paso"
         AuthType Basic
         Require valid-user
        </Directory>

[Volver](index)

---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Usar apache2.2 sin Virtual Hosting

El servidor web Apache2.2 se instala por defecto con un host virtual. La configuración de este sitio la podemos encontrar en:

        /etc/apache2/sites-available/default

Y por defecto este sitio virtual está habilitado, por lo que podemos comprobar que existe un enlace simbólico a este fichero en el directorio:

        /etc/apache2/sites-enables.

Si no necesitamos utilizar la funcionalidad de vitual hosting debemos deshabilitar el sitio virtual:

        a2dissite default

y podemos coger parte del fichero de configuración default y añadirlo a la configuración del servidor web, por ejemplo podemos ponerlo dentro del fichero /etc/apache2/apache2.conf:

        DocumentRoot /var/www
        
        <Directory /var/www/>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>

Reiniciamos el servicio y comprobamos que podemos acceder al servidor.

[Volver](index)

---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Instalación y configuración inicial del servidor web Apache 2.2
1. Instala el servidor web Apache e indica el FQDN para que al inciar el servicio no nos de ningún problema.

    Para controlar el servicio apache2 podemos usar: (para más información <http://httpd.apache.org/docs/2.2/es/stopping.html>):

        /etc/init.d/apache2 start
        /etc/init.d/apache2 stop
        /etc/init.d/apache2 restart
        /etc/init.d/apache2 reload
        /etc/init.d/apache2 status

    Tambień se puede utilizar el siguiente comando:

        service apache2 <operación>

2. ¿Qué diferencia hay entre un restart y un reload?

    También podemos utilizar la utilidad apache2ctl / apachectl:

        apache2ctl [-k start|restart|graceful|graceful-stop|stop]

3. ¿Qué es la opción graceful?

    Con esta herramienta podemos obtener también más información del servidor:

        apache2ctl -t : Comprueba la sintaxis del fichero de configuración.
        apache2ctl -M : Lista los módulos cargados
        apache2ctl -S : Lista los sitios virtuales.
        apache2ctl -V : Lista las opciones de compilación

4. Comprueba la directiva donde indicamos el puerto de escucha del servidor

5. Comprueba los módulos  cargados en el servidor: mirando en el directorio adecuado y utilizando la herramienta apache2ctl.

6. Comprueba los sitios webs activos en nuestro servidor: mirando en el directorio adecuado y utilizando la herramienta apache2ctl.

[Volver](index)

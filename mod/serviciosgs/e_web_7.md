---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Configuración básica de Apache

Busca en el fichero de configuración de Apache las siguientes directivas, determina que función tienen y el valor que poseen por defecto.

Directivas de identificación del servidor:

* [ServerName](http://httpd.apache.org/docs/2.2/mod/core.html#servername)
* [ServerAdmin](http://httpd.apache.org/docs/2.2/mod/core.html#serveradmin)
* [ServerTokens](http://httpd.apache.org/docs/2.2/mod/core.html#usecanonicalname)

Modifica el valor de ServerAdmin y ServerTokens y comprueba los resultados.

Directivas de localización de ficheros

* [DocumentRoot](http://httpd.apache.org/docs/2.2/mod/core.html#documentroot)
* [ErrorLog](http://httpd.apache.org/docs/2.2/mod/core.html#errorlog)
* [CustomLog](http://httpd.apache.org/docs/2.2/mod/mod_log_config.html#customlog)
* [LockFile](http://httpd.apache.org/docs/2.2/mod/mpm_common.html#lockfile)
* [PidFile](http://httpd.apache.org/docs/2.2/mod/mpm_common.html#pidfile)
* [ServerRoot](http://httpd.apache.org/docs/2.2/mod/core.html#serverroot)
* [AccessFileName](http://httpd.apache.org/docs/2.0/mod/core.html#accessfilename)

Directivas de control de la conexión

* [Timeout](http://httpd.apache.org/docs/2.2/mod/core.html#timeout)
* [KeepAlive](http://httpd.apache.org/docs/2.2/mod/core.html#keepalive)[Más información](http://systemadmin.es/2011/08/conexiones-con-keepalive-en-http1-0)
* [MaxKeepAliveRequests](http://httpd.apache.org/docs/2.2/mod/core.html#maxkeepaliverequests)
* [KeepAliveTimeout](http://httpd.apache.org/docs/2.2/mod/core.html#keepalivetimeout)

Otras directivas

* [User](http://httpd.apache.org/docs/2.0/mod/mpm_common.html#user)
* [Group](http://httpd.apache.org/docs/2.0/mod/mpm_common.html#group)
* [DefaultType](http://httpd.apache.org/docs/2.0/mod/core.html#defaulttype)
* [LogLevel](http://httpd.apache.org/docs/2.0/mod/core.html#loglevel)
* [LogFormat](http://httpd.apache.org/docs/2.0/mod/mod_log_config.html#logformat)

[Volver](index)

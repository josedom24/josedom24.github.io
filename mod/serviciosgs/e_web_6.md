---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Estructura de los ficheros de configuración

1) Las directivas de configuración de apache2 se pueden aplicar si está definido un determinado parámetro. Para esto se utiliza la directiva [IfDefine](http://httpd.apache.org/docs/2.2/mod/core.html#ifdefine). Busca en algún fichero de configuración esta directiva.

2) Igualmente podemos aplicar determinadas directivas si hay cargado un determinado módulo, para ello usamos [IfModule](http://httpd.apache.org/docs/2.2/mod/core.html#ifmodule). Busca alguna directiva de este tipo.

Para cargar dinámicamente los módulos se utilza la directiva [LoadModule](http://httpd.apache.org/docs/2.2/mod/mod_so.html#loadmodule), búscalos en los ficheros .load dentro de /etc/apache2/mods-availables.

Más información: <http://httpd.apache.org/docs/2.2/dso.html>

3) Busca en la configuración una variable de entorno y determina en que fichero están definidas.

4) La directiva [Include](http://httpd.apache.org/docs/2.2/mod/core.html#include) nos permite añadir ficheros de configuración a la configuración general de apache2. Comprueba qué ficheros son añadidos con esta directiva.

5) Podemos aplicar directivas a partes concretas de nuestro servidor web, para ello estudia las siguientes directivas (Para aprender más lee [Secciones de Configuración](http://httpd.apache.org/docs/2.2/sections.html)):

* [Directory](http://httpd.apache.org/docs/2.2/mod/core.html#directory)
* [DirectoryMatch](http://httpd.apache.org/docs/2.2/mod/core.html#directorymatch)
* [Files>](http://httpd.apache.org/docs/2.2/mod/core.html#files)
* [FilesMatch](http://httpd.apache.org/docs/2.2/mod/core.html#filesmatch)
* [Location](http://httpd.apache.org/docs/2.2/mod/core.html#location)
* [LocationMatch](http://httpd.apache.org/docs/2.2/mod/core.html#locationmatch)
* [VirtualHost](http://httpd.apache.org/docs/2.2/mod/core.html#virtualhost)

Localiza algunas de ellas en los ficheros de configuración.

6) ¿Qué son los ficheros .htaccess?


[Volver](index)


---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Estructura de los ficheros de configuración

1) Las directivas de configuración de apache2 se pueden aplicar si está definido un determinado parámetro. Para esto se utiliza la directiva [IfDefine](http://httpd.apache.org/docs/2.2/mod/core.html#ifdefine). Busca en algún fichero de configuración esta directiva.

2) Igualmente podemos aplicar determinadas directivas si hay cargado un determinado módulo, para ello usamos [IfModule](http://httpd.apache.org/docs/2.2/mod/core.html#ifmodule). Busca alguna directiva de este tipo.

Para cargar dinámicamente los módulos se utilza la directiva [LoadModule](http://httpd.apache.org/docs/2.2/mod/mod_so.html#loadmodule), búscalos en los ficheros *.load dentro de /etc/apache2/mods-availables.


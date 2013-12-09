---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Ejercicio: Módulos de Multiprocesamiento (MPMs)

Puedes encontrar más información en los sigientes enlaces: [Enlace 1](http://www.maestrosdelweb.com/editorial/entendiendo-los-modos-multiproceso-de-apache/) y [Enlace 2](http://yoadminsis.blogspot.com/2011/03/instalacion-y-primeros-conceptos-mpm-de.html)

Identifica en el fichero */etc/apache2/apache2.cong* las siguientes directivas de configuración e indica para que sirven:

Directivas de control de [prefork](http://httpd.apache.org/docs/2.0/mod/prefork.html)

        StartServers          5
        MinSpareServers       5
        MaxSpareServers      10
        MaxClients          150
        MaxRequestsPerChild   0


Directivas de control de [worker](http://httpd.apache.org/docs/2.0/mod/worker.html)

        StartServers          2
        MinSpareThreads      25
        MaxSpareThreads      75
        ThreadLimit          64
        ThreadsPerChild      25
        MaxClients          150
        MaxRequestsPerChild   0


[Volver](index)

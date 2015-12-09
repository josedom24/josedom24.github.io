---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Ejercicio: Módulos de Multiprocesamiento (MPMs)

Puedes encontrar más información en los sigientes enlaces: [Enlace 1](http://www.maestrosdelweb.com/editorial/entendiendo-los-modos-multiproceso-de-apache/) y [Enlace 2](http://yoadminsis.blogspot.com/2011/03/instalacion-y-primeros-conceptos-mpm-de.html)

Identifica en los ficheros de configuración de los módulos de multiprocesamiento las siguientes directivas de configuración e indica para que sirven:

En /etc/apache2/mods-availables/mpm_prefork.conf:

Directivas de control de [prefork](http://httpd.apache.org/docs/2.4/mod/prefork.html)

        StartServers          5
        MinSpareServers       5
        MaxSpareServers      10
        MaxClients          150
        MaxRequestsPerChild   0

En /etc/apache2/mods-availables/mpm_worker.conf:

Directivas de control de [worker](http://httpd.apache.org/docs/2.4/mod/worker.html)

        StartServers          2
        MinSpareThreads      25
        MaxSpareThreads      75
        ThreadLimit          64
        ThreadsPerChild      25
        MaxClients          150
        MaxRequestsPerChild   0

En /etc/apache2/mods-availables/mpm_event.conf:

Directivas de control de [event](http://httpd.apache.org/docs/2.4/mod/event.html)

        StartServers              2
        MinSpareThreads          25
        MaxSpareThreads          75
        ThreadLimit              64
        ThreadsPerChild          25
        MaxRequestWorkers       150
        MaxConnectionsPerChild    0


[Volver](index)

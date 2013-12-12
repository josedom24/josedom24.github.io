---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Ejercicio: Mediciones de rendimiento de Apache2 sirviendo páginas dinámicas

Vamos a comparar el uso de memoria y el rendimiento de Apache2 sirviendo páginas dinámicas programadas con PHP. Para ello vamos a instalar un wordpress un servidor y vamos a realizar las siguientes pruebas:

    500 peticiones y 2 concurrentes
    5000 peticiones y 10 concurrentes
    10000 peticiones y 100 concurrentes

Hay que generar gráficas de uso de memoria y rendimiento donde se vea la comparativa entre las distintas formas de ejecutar PHP:

* Módulo php5-apache2
* Módulo php5-apache2 + acelerador
* Módulo php5-apache2 + varnish
* Fastcgi + worker
* Fastcgi + worker + acelerador
* Fastcgi + worker + varnish

Lo más valorado en la tarea serán las conclusiones a las que llegas.


[Volver](index)

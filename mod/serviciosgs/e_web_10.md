---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Control de acceso

Estudia el comportamiento de [order](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#order), [allow](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#allow) y [deny](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#deny).

Un buen manual para que quede más claro lo puedes encontrar en este [enlace](http://systemadmin.es/2011/04/la-directiva-order-de-apache).

**Ejercicios**

1) Comprueba el control de acceso del directorio DocumentRoot en el host virtual default.

2) Crea un directorio en en el DocuementRoot de default llamado prohibido, que no sea accesible desde la máquina física.

3) Modifica el control de acceso para que sólo se pueda entrar al directorio prohibido desde arenita (utilizar el nombre del host).

4) Crea un escenario en Vagrant que tenga un servidor con una red publica, y una privada, un cliente conectada a la red privada. Crea un host virtual, que sólo se tenga acceso desde el cliente de la red local, y no se pueda acceder desde la anfitriona por la red pública.

[Volver](index)

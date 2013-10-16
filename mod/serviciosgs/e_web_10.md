---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Control de acceso

Estudia el comportamiento de [order](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#order), [allow](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#allow) y [deny](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#deny).

1) Comprueba el control de acceso del directorio DocumentRoot en el host virtual default.

2) Comprueba el control de acceso del directorio doc en el host virtual default.

3) Crea un directorio en en el DocuementRoot de default llamado prohibido, que no sea accesible desde la máquina física.

4) Modifica el control de acceso para que sólo se pueda entrar al directorio prohibido desde arenita (utilizar el nombre del host).

[Volver](index)

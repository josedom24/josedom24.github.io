---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Instalación y configuración básica de squid

1) Instala el proxy-cache squid3 y comprueba la configuración básica del servidor:

* Comprueba el puerto por el que está escuchando el servidor.
* Asigna como memoría de la cache 300 Mb.
* Define un tamaño de cache de 8 Gb.
* Define el máximo tamaño de los elementos cacheados a 20 Mb.
* Comprueba los ficheros de log y con que formáto se guarda la información.
* Modifica la configuración para que los errores salgan en español.

2) Una vez realizada la configuración básica, reinicia el servicio. Configura de manera manual un navegador y comienza a navegar utilizando el proxy.

¿Funciona? No, el servidor viene configurado por defecto para que sólo se puedan realizar conexiones desde localhost.

3) Para solucionar esto y poder acceder desde nuetra LAN tenemos que modificar una regla de acceso ACL:

Descomentamos una regla ACL localnet y la ponemos de la siguiente manera:

        acl localnet src 10.0.0.0/24

Descomentamos la siguiente línea que nos permite el acceso a la red que hemos definido anteriormente.

        http_access allow localnet

Reinicamos, y comprobamos: miramos el fichero /var/log/squid3/access.log, y vemos las peticiones que se han guardado en la cache.
[Volver](index)

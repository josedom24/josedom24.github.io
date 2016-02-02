---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Controlando la cache de squid

Partimos de la siguiente situación: tenemos instalado squid3 en un servidor, un navegador en la máquina real está configurado para usar el proxy (además en este navegador hemos desactivado la función de cache) y vamos acceder desde este navegador a una página html almacenada en un servidor web apache2 instalado en otro servidor.

#### Gestión de la cache por mecanismos de validación

En este primer punto vamos a acceder a la página html, y sólo va a entrar en juego el parámetro de cabacera Last-Modified. Una vez cacheada la página, si volvemos acceder a ella se preguntará al servidor si se ha modificado, el servidor responderá con la cabecera HTTP, y si la copia que tenemos es nueva se servirá directamente.

* En este caso al refrescar la página con F5 nos vamos encontrando en el fichero access.log con információn del tipo TCP_MEM_HIT o TCP_HIT, es decir acierto en la cache.
* Si modificamos la página, el servidor cambiará el parámetro Last-modified y por tanto la copia que tenemos almacendas ya no sera válida, por lo que nos bajaremos del servidor la página modificada y la volveremos almacenar. En este caso nos encontraremos en el fichero access.log una línea del tipo TCP_REFRESH_MODIFIED, indicando que la página accedida ha sido modificada.
* Si simulamos que se ha perdido la conexión con el servidor, parando el servicio apache2 en patricio, aunque se intenta verificar con el servidor si la página ha sido modificada (TCP_REFRESH_FAIL), se seguirá sirviendo la copia que tenem

#### Gestión de la cache por mecanismos de frescura

#### Expires

El parámetro Expires de la cabecera de un mensahe HTTP indica cuando o cada cuanto tiempo la página guardad en cache no es válida y por lo tanto hay que bajarse otra del servidor. Para cambiar este parámetro de la cabecera vamos a usar el mod_expire de Apache2. Para ello nos aseguramos que está activo:

        a2enmod expires

Y modificamos el fichero de configuración default de la siguiente manera:

        <Directory /var/www/>
        ExpiresActive On
        ExpiresDefault "access plus 3 seconds"
        ...

En este caso estamos diciendo que todos los ficheros alojados en /var/www tienen una caducida de 3 segundos. Cada tres segundos se va a obligar a descargarse la nueva copia del servidor.

Puedes comprobar el valor del parámetro usando el comando HEAD.

Si vamos recargando la página con F5 nos daremos cuenta que cada 3 segundos se produce un TCP_REFRESH_UNMODIFIED, es decir se obliga a la descarga de la página, durante el tiempo intermedio se supone que la página es válida.

#### Como evitar el cacheo de nuestro contenido

Como estudiado en la teoría el contenido del parámetro Control-cache de la cabecera de un mensaje HTTP indica al proxy-cache que puede hacer con dicho contenido.

Para poder modificar este parámtetro vamos a usar el mod_headers de apache2, para ello nos aseguramos que este activo:

        a2enmod headers

A continuación podemos modifcar el fichero de configuración default y añadir las siguiente líneas para evitar que se pueda cachear nuestro docuemento html:

        <Directory /var/www/>
        Header set Cache-Control "private, no-cache, no-store"
        Header set Pragma "no-cache"
        ...

En este caso cuando vamos refrescando nuestra página en el navegadorobtenemos un mensaje TCP_MISS en el fichero access.log indicando que nuestro documento no ha sido almacenado.

<div class='ejercicios' markdown='1'>
### Ejercicios 
Siguiendo el artículo [Reduciendo el tráfico usando cache en Apache](http://www.tail-f.com.ar/servicios/httpd/apache-httpd-servicios/reduciendo-el-trafico-usando-cache-en-apache.html), modifica el fichero de configuración de apache2 e implementa el ejemplo que se nos presenta y comprueba como se comportan los distintos tipos de archivos.
</div>

[Volver](index)

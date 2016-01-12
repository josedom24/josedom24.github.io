---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalar un servidor web Apache para el uso en una Intranet

#### Configuración inicial

Vamos a instalar un servidor web Apache en nuestro servidor Debian. A continuación vamos a publicar una página web de ejemplo y vamos a acceder a ella desde nuestros clientes.

#### Instalación del servidor Web

Para instalar el servidor debemos ejecutar como root el siguiente comando:

    	apt-get install apache2

Además del paquete apache2 se instalaran otros paquetes.

El fichero de configuración principal del sercidor es */etc/apache2/apache2.conf* y la configuración del sitio por defecto (default) está en el fichero */etc/apache2/sites-available/000-default.conf*

Después de cualquier cambio en la configuración debemos volver a iniciar el servicio:

    	systemctl restart apache2

Si da algún error ejecutamos la siguiente instrucción para ver los errores:

		journalctl -xn


<div class='ejercicios' markdown='1'>
##### **Ejercicios**

1. Crea dentro del directorio /var/www/html un fichero llamado entrada.html en el que pongaís un mensaje de bienvenida.

	Accede desde los clientes, poniendo en un navegador la siguiente URL: *http://direccion_ip_servidor/entrada.html*

2. A continuación vamos a publicar una página más completa en nuestro servidor, para ello bajate este [fichero .zip](files/web.zip), descomprimelo, copialo dentro de del directorio local del servidor web y accede desde el servidor y desde el cliente a la nueva pagína.

	En este caso, desde el cliente hay que poner la URL http://direccion_ip_servidor, ya que existe un fichero index.html.
</div>

#### Resolución local de nombres

Si te fijas para acceder al servidor web desde cualquier cliente de la intranet es necesario poner la dirección IP del servidor. Sería deseable acceder a la página web con un nombre, por ejemplo www.micentro.com. Para ello necesitamos convertir el nombre en dirección IP y lo vamos a hacer de forma local, sin utilizar un servidor DNS.

En primer lugar, como estamos trabajando en una intranet podemos escoger cualquier nombre de dominio, sería deseable no usar uno que ya exista en internet.

Para poder hacer la resolución local de nombres tenemos que modificar el siguiente fichero de cada clente:

* Si estamos en Windows el fichero se encuentra en *C:\Windows\System32\drivers\etc\hosts*
* Si estamos en Linux el fichero es */etc/hosts*

En este fichero tenemos que poner la dirección IP y el nombre al que corresponde en la misma línea.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

1. Modifica los ficheros hosts de los clientes y accede usando el nombre que has indicado.

</div>

[Volver](index)

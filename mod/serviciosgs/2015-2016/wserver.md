---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Configuración de un servidor Windows Server

#### Esquema de red

Debes configurar en un entorno virtual usando KVM el siguiente esquema de red:
<img width="70%" src="http://josedom24.github.io/mod/serviciosgm/img/esquema_red.png"/>

Como podemos ver, vamos a tener tres máquinas: un servidor Windows Server y dos clientes: uno Linux y otro Windows.

<div class='ejercicios' markdown='1'>
* **Tarea 1 (1 punto):**  Configuración de la red virtual en KVM. Indica el nombre que le has puesto al ordenador servidor. Y por último, indica la configuración de red del servidor y de algún cliente.
* **Tarea 2 (1 punto):**  Explica la configuración del servidor para que funcione como router y nat.
</div>

#### Servidor DHCP

Los ordenadores clientes de nuestra LAN obtienen su configuración de red ofrecidas por dicho servidor, que tiene las siguientes características:

* Rango: 192.168.1.3-192.168.1.254
* Máscara de red: 255.255.255.0 
* Puerta de enlace: La ip del router
* DNS: Según el que te convenga para hacer las pruebas 

<div class='ejercicios' markdown='1'>
* **Tarea 3 (1 punto):**  Muestra al profesor el servidor DHCP funcionando. Muestra el fichero de configuración del servidor, la lista de concesiones, la modificación en la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
</div>

Crea una reserva para el que uno de los clientes tome siempre una dirección fija.

<div class='ejercicios' markdown='1'>

* **Tarea 4 (2 puntos):** Indica las modificaciones realizadas en el servidor y muestra al profesor una comprobación de que el cliente ha tomado esa dirección.
</div>

#### Servidor DNS

Lo primero que tienes que hacer es determinar un nombre de dominio que va a ser utilizado en nuestro sistema. (En esta documentación voy a utilizar el nombre example.com). El servidor DNS ofrece el servicio de resolución de nombres para los ordenadores de nuestra red local. Debes tener en cunta los siguientes puntos:

* Cuando tengas funcionando el servidor DNS, tendrás que modificar el servidor DHCP para que los clientes usen el nuevo servidor DNS. 
* Piensa el nombre que tiene el servidor. El servidor DNS debe poder resolver los siguientes nombres: nombredelservidor.example.com, www.example.com, informatica.example.com El primero es el nombre del servidor, los dos siguientes son dos páginas webs que el servidor va a servir. 
* Debes implementar la zona inversa del servidor.

<div class='ejercicios' markdown='1'>

* **Tarea 5 (2 puntos):** Realiza la instalación y configuración del servidor DNS con las características anteriomente señaladas. Indica el cambio que hay que hacer en el servidor dhcp para que el sistema funcione de manera adecuada.. Muestra el resultado al profesor.
* **Tarea 6 (4 puntos):** Realiza las consultas dig/nslookup desde los clientes preguntando por los siguientes:
	* Dirección de www.example.com
	* El servidor DNS con autoridad sobre la zona del dominio 
	* La dirección IP de www.josedomingo.org
	* Una resolución inversa
</div>

#### Servidor WEB

El servidor tiene instalado un servidor Web IIS, que sirve dos virtual host con páginas web estáticas.

* www.example.com: Página principal del centro.
* informatica.example.com: Página del departamento de informatica
* La página www.example.com, posee un directorio /privado, que para acceder a el es necesario autentificarse.

Deficiencias que nos encontramos con este esquema

1. El servidor es un ordenador más de nuestra LAN, por lo que el cortafuegos que podemos configurar se debería implantar en el router.
2. Igualmente el dispositivo que hace NAT es el router, que puede ser insuficientes para muchos ordenadores. 
3. No se controla de ninguna manera la navegación de los clientes. 
4. El servidor web actualmente instalado solo ofrece página html estáticas. 
5. Algunos servicios que faltan: web dinámica, servicio de ftp, servicio de correos, proxy,...


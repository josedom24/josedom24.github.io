---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación y configuración de una reserva en un servidor dhcp dhcp en linux

##### Creando reservas

Veamos la sección host, en ella configuramos un host para reservar una dirección IP para él.

En una sección host debemos poner el nombre que identifica al host y los siguientes parámetros:

* hardware ethernet: Es la dirección MAC de la tarjeta de red del host.
* fixed-address: La dirección IP que le vamos a asignar. 
* Podemos usar también las opciones ya explicadas en la sección principal.

<div class='ejercicios' markdown='1'>
### Ejercicios 
1. Crea en el servidor dhcp una sección HOST para conceder a un cliente una dirección IP determinada (por ejemplo la 192.168.0.105)
2. Obtén una nueva dirección IP en el cliente y comprueba que es la que has asignado por medio de la sección host.
</div>

<div class='ejercicios' markdown='1'>
### Realiza las siguientes comprobaciones
Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstacia, para ello vamos a poner un tiempo de conseción muy bajo.
1. Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
2. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
</div>


[Volver](index)


---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Proyecto 2: Instalación de un servidor en un centro educativo

Un centro educativo ha comprado un servidor, en el que se va instalar una distribución Debian, y que se va a instalar siguiendo este esquema de red:

![Esquema de red](img/esquema_red2.png)

#### Instalación de las máquinas

Vamos a utilizar VirualBox para simular las máquinas que necesitamos en nuestro esquema de trabajo, en nuestro proyecto vamos a necesitar 3 máquinas virtuales:

* Un servidor, donde instalaremos Debian 7.0
* Un cliente, donde se instalará Windows 7 
* Un cliente, donde se instalará Ubuntu 

#### Servidor Debian

Vamos a crear una nueva máquina donde vamos a instalar el servidor con Debian:

* Durante la instalación se pondrá el nombre del servidor
* La instalación se hará sin entorno gráfico
* Recuerda que nuestro servidor va a tener dos tarjetas de red: una modo puente que va a conectar con nuestra LAN del instituto, y otra modo red interna que nos conectarás con los clientes.

##### Adaptador modo puente

Definimos la primera interfaz virtual en modo puente, en nuestro servidor será la interfaz eth0. Configuramos eth0 para que tome la configuración de red de forma dinámica.

##### Adaptador modo red interna

Será la interfaz eth1 de nuestro servidor. Configuramos eth1 para que tenga direccionamiento estático con la siguiente configuración:

* Dirección IP: 192.168.1.254
* Mascara de red: 255.255.255.0
* Broadcast: 192.168.1.255
* Red: 192.168.1.0



#### Enrutador

Como se observa en el esquema nuestro ordenador va a tener dos tarjetas de red, por lo tanto va a ser el responsable de gestionar la comunicación que entra y sale de nuestra red local. En una segunda fase de nuestra implantación (esto se estudiará en la asignatura de seguridad) se implantará un cortafuego en este equipo. Lo que tenemos que configurar este equipo para que enrute y haga la función de NAT.

##### Configuración del enrutamiento


Modificamos el fichero /etc/sysctl.conf descomentando la siguiente línea:

        net.ipv4.ip_forward=1

Para que nuestros clientes tengan acceso a internet, debemos configurar el fichero /etc/network/interfaces y añadir las siguientes líneas:

        allow-hotplug eth1 
        iface eth1 inet static 
        ...
        up iptables -t nat -A POSTROUTING -o eth0 -s 192.168.1.0/24 -j MASQUERADE
        down iptables -t nat -D POSTROUTING -o eth0 -s 192.168.1.0/24 -j MASQUERADE

<div class='ejercicios' markdown='1'>
##### **Instalación y configuración inicial**
1. Empieza con una introducción, donde se explique el objetivo del proyecto que vas a realizar y a continuación inserta un ["Seguir leyendo..."](http://lgredsocial.wordpress.com/2012/02/14/como-poner-seguir-leyendo/)
2. Tienes que pensar un nombre para el instituto, y a partir de ese nombre piensa un nombre de dominio que suponemos que ha comprado el centro.
3. Explica la instlación del servidor (Suponemos que los clientes ya lo tenemos instalados)
4. Configura de forma adecuada el nombre del servidor totalmente cualificado. Ejecute la instrucción hostname -f
5. Explica la configuración de red del servidor.
6. Debe aparecer la salida del comando ifconfig en el servidor.
7. Explica la configuración para el servidor haga de enrutador.
8. Se debe hacer una prueba de funcionamiento del enrutamiento desde los dos clientes.
</div>

#### Servidor DHCP

Los ordenadores clientes de nuestra LAN obtienen su configuración de red ofrecidas por dicho servidor, que tiene las siguientes características:

* Rango: 192.168.1.3-192.168.1.253
* Máscara de red: 255.255.255.0 
* Puerta de enlace: La ip del servidor
* Nombre de dominio
* DNS: 192.168.102.2

Vamos a suponer que el cliente linux es un ordenador del equipo directivo que debe tener la dirección ip 192.168.1.200. Configura una reserva en el servidor dhcp.

<div class='ejercicios' markdown='1'>
##### **DHCP**
1. Empieza con una introducción y a continuación inserta un "Seguir leyendo..."
2. Explica la instalación y configuración del servidor dhcp
3. Prueba de funcionamiento (Concesiones de direcciones)
4. Prueba de funcionamiento de la reserva
</div>

[Volver](index)

---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación de máquinas virtuales (Linux)

Vamos a utilizar VirualBox para simular las máquinas que necesitamos en nuestro esquema de trabajo,en nuestras prácticas vamos a necesitar 3 máquinas virtuales:


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

* Dirección IP: 192.168.0.1
* Mascara de red: 255.255.255.0
* Broadcast: 192.168.0.255
* Red: 192.168.0.0

##### Configuración del enrutamiento


Modificamos el fichero /etc/sysctl.conf descomentando la siguiente línea:

        net.ipv4.ip_forward=1

Para que nuestros clientes tengan acceso a internet, debemos configurar el fichero /etc/network/interfaces y añadir las siguientes líneas:

        allow-hotplug eth1 
        iface eth1 inet static 
        ...
        up iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
        down iptables -t nat -D POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE


[Volver](index)


---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración básica de red

####  Configurando las interfaces de red

**IP Estática**

La configuración de las interfaces de red se encuentran en el fichero:

        /etc/network/interfaces


Un ejemplo de este fichero puede ser el siguiente:

        # The loopback network interface
        auto lo
        iface lo inet loopback
        # The primary network interface
        auto eth0
        iface eth0 inet static
        address 200.89.74.17
        netmask 255.255.255.0
        network 200.89.74.0
        broadcast 200.89.74.255
        gateway 200.89.74.1

La primera interfaz loopback (lo) es una interfaz especial que permite hacer conexiones internas. Esta no debería modificarse bajo ningún motivo. La segunda interfaz definida es eth0, que corresponde a la primera interfaz Ethernet.

* La entrada address corresponde al número IP del ordenador.
* La entrada netmask corresponde a la máscara de red.
* Las entradas network y broadcast casi siempre corresponden al primer y último número del rango de números IP.
* La entrada gateway define el número IP de la puerta de enlace.

Cada vez que se cambie la configuración de red debes reiniciar el demonio de red con la siguiente intrucción:

        /etc/int.d/networking restart


**IP dinámica**

Para configurar la red para que toma una dirección dinámica de un servidor DHCP, la configuración de eth0 debe ser:

        # The primary network interface
        auto eth0
        iface eth0 inet dhcp

####Instrucciones para gestionar las interfaces de red
**ifconfig**

Con esta instrucción puedes visualizar la configuración actual de red.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1) Configura la interface de red con una ip fija y comprueba con ifconfig que se ha configurado correctamente.

2) Configura la interface de red para obtener una IP dinámica y comprueba con ifconfig la configuración que ha tomado.

</div>

**ifup y ifdown**

Con estas instrucciones puedes desconectar (ifdown) y conectar (ifup) la interface de red que desees, por ejemplo:

        ifdown eth0


#### Configurando los nombres de la máquina y la resolución DNS
**/etc/nsswitch.conf**

En este fichero se especifican los métodos de resolución de nombres del equipo, por ejemplo existe una línea:

        hosts: files dns

que nos dice dónde y en qué orden va a buscar la relación entre nombres de equipo y direcciones IP, en este caso en ficheros y servidores DNS.

**/etc/hostname**

En este fichero se encuentra el nombre de la máquina.

Para obtener el nombre de la máquina puedes utilizar la instrucción *hostname*.

**/etc/hosts**

En este fichero se encuentra las resoluciones estáticas de DNS, en este fichero indicamos la relación entre direcciones IP y nombres.

Si usamos la siguiente instrucción:

        hostname -f
        hostname: Unknown host

El mensaje de Unknown host, significa que nuestro sistema no tiene un FQDN (Fully Qualified Domain Name es un nombre que incluye el nombre de la computadora y el nombre de dominio asociado a ese equipo). Lo resolvemos agregando nuestro domino al nombre del host, en el formato IP nombre_host.dominio.com, de esta manera de ejemplo:

        nano /etc/hosts

        192.168.1.1 mi_maquina.mi_dominio.com mi_maquina


**/etc/resolv.conf**

En este fichero se encuentra las direcciones de los servidores DNS, que nos van a permitir la traducción de nombres a direcciones IP.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

1) Cambia el nombre de tu máquina.

2) Modifica el fichero hosts, e introduce tu dirección IP con el nombre de máquina y el FQDN.

3) Edita el fichero /etc/resolv.conf, comprueba los servidores DNS que están configurados y cámbialos por los siguientes (194.224.52.36 y 194.224.52.37)

</div>

[Volver](index)


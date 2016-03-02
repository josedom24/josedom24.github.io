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

#### Servidor Web

Una de los principales servicios que va a ofrecer nuestro servidor es una página web con las siguientes características:

* Tienes que escoger un nombre de dominio que vas a utilizar (elije un nombre según el nombre del instituto), para este documento voy a utilizar dominio.com.
* La página principal del insituto será www.dominio.com donde podrás encontrar información y noticias sobre el instituto (utiliza una plantilla modificada con el nombre del insitituto para que parezca una página real).
* La página www.dominio.com/documentos, muestra una lista con toda la documentación pública del instituto. Toda esta documentación estará en el directorio /srv/doc
* Cada profesor tiene un usuario en el servidor, además existen usuarios especiales: director, jefeestudios, secretario,...
* La página www.dominio.com/profesores, es una zona privada donde tienen accesos todos los usuarios, sin embargo a la página www.dominio.com/equipodirectivo sólo tienen accesos los usuarios del equipo directivo: director, jefeestudios, secretario,...
* Cada uno de los profesores puede gestionar su propia página web, para ello activa el módulo mod_userdir.
* El departamento de informática posee una página web realizada con moodle, que se accede en informatica.dominio.com

<div class='ejercicios' markdown='1'>
##### **WEB**
1. Explica la instalación del servidor web.
2. Se valorará positivamente la plantilla escogida y la modificación que se haga para que parezca una página real. Utiliza la misma plantilla para todas las páginas del sitio.
3. Explica como has configurado el servidor para mostrar la página www.dominio.com/documentos.
4. Autentificación: Explica como se crean los usuarios y cómo se configura las distintas páginas (www.dominio.com/profesores, www.dominio.com/equipodirectivo) para configurar la autentificación.
5. Invenstiga como activar el módulo mod_userdir, ¿para qué sirve? Pon algún ejemplo para comprobar el funcionamiento. 
6. Explica la instalación de un servidor LAMP.
7. Realiza una pequeña guía (no hace falta poner capturas de pantalla) de instalación de moodle. También tienes que explicar la configuración del nuevo virtual hosts.
</div>

#### Servidor DNS

Queremos centralizar la gestión de los nombres de las máquinas de nuestro dominio instalando un DNS en nuestro servidor, además podremos conseguir aumentar la velocidad de navegación de nuestros clientes. Para ello vamos a instalar en nuestro servidor debian un servidor DNS bind9 con las siguientes características:

* Tiene que tener configurada una zona de resolución directa y otra zona de resolución inversa.
* Todos los clientes deben utilizar este servidor DNS para realizar la resolución de nombres.

<div class='ejercicios' markdown='1'>
##### **DNS**
1. Explica razonadamente la afirmación: " instalando un DNS en nuestro servidor, además podremos conseguir aumentar la velocidad de navegación de nuestros clientes"
2. Explica cómo se instala el servidor DNS y configura el servidor de manera adecuada, muestra los archivos necesarios tras la configuración. Debes decidir, teniendo en cuenta el punto anterior, los nombres que debe resolver el servidor (el cliente que tiene hecha la reserva DHCP también se debe resolver).
3. ¿Qué modificación debes hacer en el servidor DHCP para qué los clientes utilicen el servidor DNS?
4. Muestra desde los clientes, las consultas dns hechas con dig y nslookup que respondan:

* Servidor dns de dominio.com
* Dirección ip de informatica.dominio.com
* Nombre de la dirección ip del servidor (resolución inversa)
* Dirección ip de www.josedomingo.org
</div>

#### Servidor FTP

Para facilitar el acceso al servidor hemos instalado un servidor ftp proftpd, con la siguiente funcionalidad:

* Si se accede de forma autentificada cada usuario accederá a su carpeta public_html, donde podrá gestionar los archivos de su página web personal.
* Si se accede de forma anónima, se accederá al directorio /srv/doc, donde está toda la documentación pública del instituto (la misma carpeta a la que se accede por medio de http://www.dominio.com/documentos).

<div class='ejercicios' markdown='1'>
##### **FTP**
1. Explica la modificación en el servidor DNS para que los usuarios puedan acceder al nombre ftp.dominio.com
2. Explica como se instala el servidor proftpd y la configuración que necesita.
3. Muestra un acceso autentificado al servidor con un cliente gráfico.
4. Muestra un acceso anónimo al servidor con un cliente gráfico.
</div>

#### Acceso remoto

Para facilitar la administración por parte de los técnicos de los clientes linux vamos a configurar el sistema para que se pueda acceder remotamente de dos formas:

* Por seguridad se va a realizar la conexión utilizando el puerto 2222.
* SSH con claves públicas: Desde el servidor, el administrador del sistema va a poder acceder a los clientes linux mediante ssh con clave pública, por lo que no será necerario que introduzca la contraseña.
* Escritorio remoto con VNC: Se puede acceder con un cliente de escritorio remoto a los clientes linux, pero es necesario poner una contraseña de acceso, qué sólo saben los técnicos.

<div class='ejercicios' markdown='1'>
##### **Acceso remoto**
1. Escribe un manual donde expliques  la configuración necesaria para  que se pueda acceder a una máquina por ssh utilizando clave pública, por el puerto 2222.
2. Muestra la configuración en linux para permitir el acceso remoto por VNC, y muestra algunas capturas de pantalla (con Windows y Linux) accediendo por escritorio remoto.
</div>

#### Servidor Correos

Queremos ofrecer en nuestro sistema el servicio de correo electrónico para permitir que los usuarios del servidor puedan mandarse correos. Para ello vamos a instalar un servidor postfix. Nuestro sistema de c$

* Crearemos un nuevo nombre smtp.dominio.com que será el servidor de correos saliente.
* Crearemos un servidor mail.dominio.com que será un servidor de correo pop.
* Los usuarios tendrán en sus ordenadores clientes de correo que podrán utilizar usando  los dos servidores anteriores.
* Además usando el protocolo imap, y un cliente web de correos (squirredmail) podrán gestionar sus correos desde la URL correo.dominio.com

<div class='ejercicios' markdown='1'>

#### **Servidor de correos**

1. Describe la instlación y configuración del servidor postfix.
2. Muestra una prueba de envío y recepción de correo desde el servidor usando el comando mail. Muestra también la salida del log.
3. Explica la instalación y configuración del servidor pop e imap.
4. Muestra la configuración del cliente de correos (servidor de correo saliente y servidor de correos pop).
5. Explica la instalación de squirrelmail y la configuración necesaria para que se pueda acceder desde la URL indicada anteriormente.
6. Con captura de pantalla demuestra el envío de un correo desde el squirredmail y la recepción por parte del usuario destinatario usando un cliente de correos.
</div>


[Volver](index)

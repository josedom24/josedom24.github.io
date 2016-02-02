---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
# Proyecto 1: Instalación de un servidor en un centro educativo

## Entrega 2: Escenario Linux Debian

Lo primero que tienes que hacer es elegir un nombre de dominio.

1. Configura en kvm el esquema de red del punto 2.

	* Configuración de la red virtual
	* No hace falta explicar la instalación de los sistemas operatvios
	* Configuración de red del servidor y de algún cliente

2. Punto 2a: Enrutador

	* Explica la configuración del servidor para que haga de enrutador

3. Punto 2b: Instalación y configuración del servidor DHCP. Implementa una reserva. 

	* Instalación del servidor dhcp
	* Configuración del servidor dhcp
	* Prueba de funcionamiento (Concesiones de direcciones)
	* Prueba de funcionamiento de la reserva

4. Realizar el punto 2c) Servidor web, teniendo en cuenta los siguientes puntos:

	* Modifica los gestores de contenidos un poco para que parezcan que son las páginas reales del instituto, pon un título, algún logotipo, cambia los temas,...
	* Explica como has configurado los dos virtual hosts
	* Explica la instlación de un servidor LAMP. (No hace falta explicar la instlación de wordpress)
	* Explica el proceso de instalación de phpmyadmin y la configuración necesaria para que sólo sea accesible desde la red local.
	* Explica las modificación de la configuración para conseguir lo que se pide en el punto 4.
	* Explica la instalación y configuración del módulo userdir. Presenta algún ejemplo donde se vea que podemos cambiar la configuración por medio de ficheros .htaccess.
	* Explica los pasos necesarios para instalar webalizer para cada uno de los sitios webs.
	* Explica las modificación de la configuración para conseguir lo que se pide en el punto 8.
	* Explica como conseguir las URL "limpias" en wordpress.

5. Realizar el punto 2d) Servidor DNS, teniendo en cuenta estos puntos:

	* Modificación en el servidor DHCP para que los clientes usen el nuevo DNS
	* Una vez terminado de realizar la configuración, se debe entregar las salidas del comando nslookup y dig desde los clientes windows y linux.
	* Se debe entregar el repositorio github donde guardas el script gestionDNS.py con un pequeño manual de como funciona.
	* **[OPTATIVO]]**: Configura el servidor DNS dinámico para que se pueda resolver los nombres de los clientes que reciben configuración de red dinámica.

[Volver](index)

---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Instalación y configuración del servidor dhcp en linux

Después de leer la documentación, instala el servidor dhcp. Recuerda que al inicializar el servicio nos dará un error, esto es debido a que no hemos configurado el servidor.

#### Instalación del servidor isc-dhcp-server

Para instalar nuestro servidor dhcp ejecutamos:

	apt-get install isc-dhcp-server

<div class='nota' markdown='1'>
### Nota
Cuando instalamos el servidor por primera se produce un error, ya que no está configurado. Puedes ver los errores producidos por el servidor en el fichero /var/log/syslog
</div>

#### Configuración del servidor isc-dhcp-server

Lo primero que tenemos que hacer es configurar el interfaz de red por el que va a trabajar el servidor dhcp, para ello editamos el siguiente fichero:

	/etc/default/isc-dhcp-server

Donde configuramos el parámetro interfaces, por ejemplo:
	
	INTERFACES="eth1"
 
El fichero principal de configuración de DHCP es:

	/etc/dhcp/dhcpd.conf

El fichero de configuración está dividido en dos partes:

* Parte principal (valores por defecto): especifica los parámetros generales que definen la concesión y los parámetros adicionales que se proporcionarán al cliente.
* Secciones (concretan a la principal)
     * Subnet: Especifican rangos de direcciones IPs que serán cedidas a los clientes que lo soliciten.
     * Host: Especificaciones concretas de equipos.

En la parte principal podemos configurar los siguientes parámetros, que más tarde podremos reescribir en las distintas secciones:


* max-lease-time: Tiempo de la concesión de la dirección IP
* default-lease-time: Tiempo de renovación de la concesión
* option routers: Indicamos la dirección red de la puerta de enlace que se utiliza para salir a internet.
* option domain-name-server: Se pone las direcciones IP de los servidores DNS que va a utilizar el cliente.
* option domain­-name: Nombre del dominio que se manda al cliente.
* option subnet­mask: Subred enviada a los clientes.
* option broadcast-­address: Dirección de difusión de la red.

Al indicar una sección subnet tenemos que indicar la dirección de la red y la mascara de red y entre llaves podemos poner los siguientes parámetros:

* range: Indicamos el rango de direcciones IP que vamos a asignar.
* Alguno de los parámetros que hemos explicado en la sección principal.

Ejemplo de configuración de la sección subnet puede ser:

	subnet 192.168.0.0 netmask 255.255.255.0 {
	  range 192.168.0.60 192.168.0.90;
	  option routers 192.168.0.254;
	  option domain­name­servers 80.58.0.33, 80.58.32.9;
	}
	
Sólo falta configurar los clientes para que tomem la configuración de red de forma dinámica.



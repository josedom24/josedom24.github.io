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
 

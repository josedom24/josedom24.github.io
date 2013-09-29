---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de un servidor DHCP en Windows Server 2008 (1)

En esta práctica vamos a instalar y configurar un servidor DHCP en nuestro servidor, con todas las opciones de configuración.
Vamos a instalar en nuestro servidor windows server2008 un servidor DHCP y vamos a probar su funcionamiento en nuestros dos 
clientes.
Pasos a seguir:

#### Instala rol de servidor DHCP

Los servidores suelen tener su configuración de red de forma estática, en nuestro caso el servidor va a conceder las configuraciones de red por la interfaz de red virtual (modo red interna) que tiene una configuración estática:

* Dirección IP: 192.168.0.1
* Máscara de red: 255.255.255.0

#### Configura el servidor DHCP con las siguientes características

* Ámbito: iesgn
* Rango de direcciones a repartir: 192.168.0.100 - 192.168.0.110
* Máscara de red: 255.255.255.0
* Duración de la concesión: 1 hora
* Puerta de enlace: 192.168.0.1
* Servidores DNS: 8.8.8.8, 8.8.4.4
* Sin servidores WINS

#### Configura los clientes

Cambia la configuración del cliente para que tome una configuración de forma dinámica.




---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Proyecto 1: Configuración de un servidor Windows Server

Te han contratado como administrador de redes en una empresa que posee una red de ordenadores con varios clientes 
y un servidor donde se ha instalado un sistema operativo Windows 2008. Actualmente la dirección de la empresa quiere 
mejorar la gestión de la red y ese es tu objetivo. Quieren mejorar los siguientes aspectos de la red:
* Actualmente la configuración de red de los cliente se hacía de forma estática, en un segmento de direcciones 192.168.2.0/24. Quieren tener un sistema de asignación dinámica de direcciones IP.
* Quieren crear varias páginas web para dar servicio a la intranet para ello han contratado un dominio masterlan.com
* Todos los usuarios deben tener la posibilidad de publicar su propia página web.
* Para poder acceder a los distintas máquinas de la intranet, se necesita que instales un servidor DNS.
* Los usuarios deben tener la posibilidad de gestionar su página web por medio de un servidor ftp.
* Los documentos importantes de la empresa deben ser accesible desde un servidor ftp anónimo.
* Un grupo de usuarios (los técnicos) pueden gestionar el servidor de forma remota.
* Todos los usuarios deben poseer una cuenta de correos de la forma usuario@masterlan.com

#### Servidor DHCP

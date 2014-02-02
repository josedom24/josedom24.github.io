---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación y configuración del servidor bind9 en nuestra red local

<div class='notas' markdown='1'>
#### Nota importante

Desinstala el servidor dnsmasq que has instalado en la práctica anterior para que no tengas conflictos.
</div>

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red, vamos a instalar el servidor DNS en nuestro servidor debian. Las características del servidor DNS que queremos instalar son las siguientes:

* Vamos a crear una zona para el dominio: iesgn.org
* Vamos a crear una zona de resolución inversa.
* Suponemos que el nombre del servidor es *miservidor*.
* Vamos a suponer que tenemos un servidor ftp que se llame ftp.iesgn.org y que está en 192.168.1.201 (esto es ficticio)
* Además queremos nombrar al cliente que tenía asignada una reserva: lisa.
* Suponemos que tenemos dos sitios webs: www.iesgn.org y departamentos.iesgn.org


<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1. Configura los clientes e indica que su DNS es nuestro servidor. Si tienes un servidor DHCP modifícalo para que envíe el nuevo DNS a los clientes.
2. Comprueba el funcionamiento usando el comando dig/nslookup desde los clientes preguntando or la dirección de los distintos nombres, el servidor con autoridad para la zona iesgn.org, comprueba que el servidor DNS hace de forwarder preguntando con dig/nslookup la dirección ip de  www.josedomingo.org.
3. Comprueba que puedes acceder a las páginas www.iesgn.com y departamentos.iesgn.com
</div>
[Volver](index)

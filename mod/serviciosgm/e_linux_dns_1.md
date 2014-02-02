---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: DNSmasq como DNS cache/forward en una red local

*El paquete dnsmasq permite poner en marcha un servidor DNS de una forma muy sencilla. Simplemente instalando y arrancando el servicio dnsmasq, sin realizar ningún tipo de configuración adicional, nuestro PC se convertirá en un servidor caché DNS y además, resolverá los nombres que tengamos configurados en el archivo /etc/hosts de nuestro servidor. La resolución funcionará tanto en sentido directo como en sentido inverso, es decir, resolverá la IP dado un nombre de PC y el nombre del PC dada la IP.*

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red, vamos a instalar el servidor DNS en el mismo ordenador que tenemos instalado el servidor web. Las características del servidor DNS que queremos instalar son las siguientes:

* El dominio que hemos elegido es iesgn.org
* Suponemos que el nombre del servidor es *miservidor*.
* Vamos a suponer que tenemos un servidor ftp que se llame ftp.iesgn.org y que está en 192.168.1.201 (esto es ficticio)
* Además queremos nombrar al cliente que tenía asignada una reserva: lisa.
* Suponemos que tenemos dos sitios webs: www.iesgn.org y departamentos.iesgn.org

Por lo tanto los nombres que debe conocer los clientes son:

* *miservidor*.iesgn.org
* ftp.iesgn.org
* lisa.iesgn.org
* www.iesgn.org
* departamentos.iesgn.org

Para instalar el servicio:

        apt-get install dnsmasq

A continuación, editamos el fichero /etc/dnsmasq.conf y modificamos las siguientes líneas:

* Descomentamos strict-order para que se realicen las peticiones DNS a los servidores que aparecen en el fichero /etc/resolv.conf en el orden en el aparecen.
* Incluimos las interfaces de red que deben aceptar peticiones DNS, descomentando la línea interface por ejemplo: interface=eth0

Para arrancar y parar el servicio

        service dnsmasq restart

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1. Configura los clientes e indica que su DNS es nuestro servidor. Si tienes un servidor DHCP modifícalo para que envíe el nuevo DNS a los clientes.
2. Comprueba el funcionamiento usando el comando dig/nslookup desde los clientes preguntando por los distintos nombres. Comprueba que el servidor DNS hace de forwarder preguntando con dig/nslookup la dirección ip de  www.josedomingo.org.
3. Comprueba que puedes acceder a las páginas www.iesgn.org y departamentos.iesgn.org
</div>
[Volver](index)

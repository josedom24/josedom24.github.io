---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación de un servidor DNS local con Windows 2008 Server
<div class='nota' markdown='1'>
**IMPORTANTE**

1. Modifica el fichero hosts y borra todas las líneas que has incluido en prácticas anteriores, sólo debes dejar la del localhost.

2. Para esta práctica se necesita configurar IIS de forma similar a la práctica: Configuración de sitios web virtuales usando IIS, por lo tanto debes tener el IIS configurado y crear dos sitios webs: www.iesgn.com y departamentos.iesgn.com
</div>

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red, vamos a instalar el servidor DNS en nuestro servidor. El dominio con el que vamos a trabajar es iesgn.com, y la red la 192.168.1.0, la ip del servidor es la 192.168.1.1


1. Vamos a crear una zona para el dominio: iesgn.com
2. Vamos a crear una zona de resolución inversa: 1.168.192.in-addr.arpa
3. Vamos a tener los siguientes FQHN:

	* El servidor DNS (192.168.1.1) se llama joker.iesgn.com
	* batman.iesgn.com (192.168.1.2, pon la configuración de red estática).
    * robin.iesgn.com (192,.168.1.3, pon la configuración de red estática).
    * cat.iesgn.com (192.168.1.202) (esto es ficticio)
    * pinguino.iesgn.com (192.168.1.203) (esto es ficticio)
    * doscaras.iesgn.com (192.168.1.204) (esto es ficticio)
	* Vamos a suponer que tenemos un servidor para recibir los correos que se llame correo.iesgn.com y que está en 192.168.1.205 (esto es ficticio)
	* Vamos a suponer que tenemos un servidor ftp que se llame ftp.iesgn.com y que está en 192.168.1.202 (esto es ficticio)
	* www.iesgn.com esta alojado en el IIS del servidor.
    * departamentos.iesgn.com esta alojado en el IIS del servidor.

<div class='ejercicios' markdown='1'>
**Ejercicios**

1. Configura el servidor DNS con los registros A, CNAME, MX y NS necesarios. Configura el SOA. Entrega una captura de la pantalla de la configuración principal del servidor.

2. Configura los clientes para que su DNS sea el servidor Windows 2008, debes indicar en la configuración de red del cliente como DNS primario la ip del mservidor. 

3. Comprueba el funcionamiento utilizando los comandos nslookup / dig desde los clientes preguntando por los siguientes:

	* Dirección de joker.iesgn.com, www.iesgn.com, ftp.iesgn.com, batman.iesgn.com
	* El servidor DNS que tiene configurado la zona del dominio iesgn.com
	* El servidor de correo configurado para iesgn.com
	* La dirección IP de www.josedomingo.org

4. Comprueba que se puede acceder a las páginas web desde los clientes.

</div>
[Volver](index)

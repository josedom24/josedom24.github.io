---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Ejercicio completo del servidor DNS (Tiempo estimado: 12 horas)

#### Escenario

1. En nuestra red local tenemos un servidor Web que sirve dos páginas web: *www.iesgn.org*, *departamento.iesgn.org*
2. Vamos a instalar en nuestra red local un servidor DNS (lo puedes instalar en el mismo equipo que tiene el servidor web)
3. Voy a suponer en este documento que el nombre del servidor DNS va a ser *pandora.iesgn.org*

#### Ejercicios

1. Instala el servidor dns **dnsmasq** en *pandora.iesgn.org* y configúralo para que los clientes puedan conocer los nombres necesarios.

	* Modifica los clientes para que utilicen el nuevo servidor dns.
	* Realiza una consulta a www.iesgn.org, y a www.josedomingo.org.
	* Realiza una prueba de funcionamiento para comprobar que el servidor dnsmasq funciona como cache dns.

2. Desinstala el servidor **dnsmasq** del ejercicio anterior e instala un servidor dns **bind9**.  Las características del servidor DNS que queremos instalar son las siguientes:

	* El servidor DNS se llama *pandora.iesgn.org* y por supuesto, va a ser el servidor con autoridad para la zona *iesgn.org*..
	* Vamos a suponer que tenemos un servidor para recibir los correos que se llame correo.iesgn.org y que está en la dirección x.x.x.200 (esto es ficticio).
	* Vamos a suponer que tenemos un servidor ftp que se llame ftp.iesgn.org y que está en x.x.x.201 (esto es ficticio)
	* Además queremos nombrar a los clientes.
	* También hay que nombrar a los virtual hosts de apache: www.iesgn.org y departementos.iesgn.org
	* Se tienen que configurar la zona de resolución inversa.

	Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:

	* Dirección de *pandora.iesgn.org*, www.iesgn.org, ftp.iesgn.org
	* El servidor DNS con autoridad sobre la zona del dominio iesgn.org
	* El servidor de correo configurado para iesgn.org
	* La dirección IP de www.josedomingo.org
	* Un resolución inversa

3. El servidor DNS actual funciona como **DNS maestro**. Vamos a instalar un nuevo servidor DNS que va a estar configurado como **DNS esclavo** del anterior, donde se van a ir copiando periódicamente las zonas del DNS maestro. Suponemos que el nombre del servidor DNS esclavo se va llamar *afrodita.iesgn.org*.

	* Entrega la configuración de las zonas del maestro y del esclavo.
	* Comprueba si las zonas definidas en el maestro tienen algún error con el comando adecuado.
	* Comprueba si la configuración de named.conf tiene algún error con el comando adecuado.
	* Reinicia los servidores y comprueba en los logs si hay algún error. **No olvides incrementar el número de serie en el registro SOA si has modificado la zona en el maestro**.
	* Muestra la salida del log donde se demuestra que se ha realizado la transferencia de zona.
	* Realiza una consulta con dig tanto al maestro como al esclavo para comprobar que las respuestas son autorizadas. ¿En qué te tienes que fijar?
	* Configura un cliente para que utilice los dos servidores como servidores DNS.
	* Solicita una copia completa de la zona desde el cliente ¿qué tiene que ocurrir?. Solicita una copia completa desde el esclavo ¿qué tiene que ocurrir?
	* Realiza una consulta desde el cliente y comprueba que servidor está respondiendo.
	* Posteriormente apaga el servidor maestro y vuelve a realizar una consulta desde el cliente ¿quién responde?

4. Tenemos un servidor DNS que gestiona la zona correspondiente al nombre de dominio *iesgn.org*, en esta ocasión queremos delegar el subdominio *informatica.iesgn.org* para que lo gestione otro servidor DNS. Por lo tanto tenemos un escenario con dos servidores DNS:

* *pandora.iesgn.org*, es servidor DNS autorizado para la zona **iesgn.org**.
* *ns.informatica.iesgn.org*, es el servidor DNS para la zona **informatica.iesgn.org** y, está instlado en otra máquina.

	Los nombres que vamos a tener en ese subdominio son los siguientes:

	* **www.informatica.iesgn.org** corresponde a un sitio web que está alojado en el servidor web del departamento de informática.
	* Vamos a suponer que tenemos un servidor ftp que se llame **ftp.informatica.iesgn.org** y que está en la misma máquina.
	*  Vamos a suponer que tenemos un servidor para recibir los correos que se llame **correo.informatica.iesgn.org**.

	Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:	

	* Dirección de www.informatica.iesgn.org, ftp.informatica.iesgn.org
	* El servidor DNS que tiene configurado la zona del dominio informatica.iesgn.org. ¿Es el mismo que el servidor DNS con autoridad para la zona iesgn.org?
	* El servidor de correo configurado para informatica.iesgn.org

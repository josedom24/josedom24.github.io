---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Servidor de correos

#### (11 tareas - 30 puntos)(5 tareas obligatorias - 8 puntos)

Esta tarea consiste en instalar y configurar un servidor de correo similar al de cualquier organización, capaz de enviar y recibir directamente correo, almacenar los usuarios en LDAP, filtrar el correo en busca de virus o spam y servirlo a sus usuarios a través de los protocolos POP, IMAP y configurar un Webmail.

### Objetivos

1. Instalar y configurar un servidor postfix en un equipo con dirección IP pública dinámica
2. Aprender a configurar todos los componentes de un servidor de correos completo
3. Depurar el funcionamiento de un servicio
4. Documentar adecuadamente todo el proceso

### Pasos a realizar


#### En clase

* Vamos a realizar un sistema de correo para el dominio tudominio.gonzalonazareno.org, cuyo servidor DNS lo administras en la máquina piolin. Tienes que comunicar el nombre de dominio al profesor para configurar el servidor de correos del departamento.
* Instala postfix en la máquina piolín y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.)
* Configura tu servidor de correos para que use a babuino como relay.

<div class='ejercicios' markdown='1'>

* **Tarea 1 (1 puntos)(Obligatorio):** Docuementa en redmine una prueba de funcionamiento, donde envíes desde tu servidor local al exterior. Muestra el log donde se vea el envío.
* **Tarea 2 (1 puntos)(Obligatorio):** Documenta en redmine una prueba de funcionamiento, donde envíes un correo desde el exterior(gmail, hotmail,...) a tu servidor local. Muestra el log donde se vea el envío.
</div>

* Instala y configura un servidor dovecot POP e IMAP en tu equipo
* Configura adecuadamente un cliente de correo (evolution, outlook, thunderbird, ...) para que reciba el correo a través de POP o IMAP. El cliente debe estar configurado en una máquina cliente. Nombra en tu servidor DNS al servidor smtp, pop e imap.

<div class='ejercicios' markdown='1'>
* **Tarea 3 (2 puntos)(Obligatorio):** Docuementa en redmine una prueba de funcionamiento, donde envíes desde tu cliente de correos al exterior. ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración).
* **Tarea 4 (2 puntos)(Obligatorio):** Documenta en redmine una prueba de funcionamiento, donde recibas un correo desde el exterior(gmail, hotmail,...) y lo leas en tu cliente de correo. Utiliza el protocolo POP.  ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración). Muestra una prueba de funcionamiento de cómo funciona el protocolo POP.
* **Tarea 5 (2 puntos)(Obligatorio):** Documenta en redmine una prueba de funcionamiento, donde recibas un correo desde el exterior(gmail, hotmail,...) y lo leas en tu cliente de correo. Utiliza el protocolo IMAP.  ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración). Muestra una prueba de funcionamiento de cómo funciona el protocolo IMAP.
</div>

* Instala un webmail (roundcube) para gestionar el correo del equipo mediante una interfaz web.
* Instala y configura correctamente un sistema de filtrado de virus y spam utilizando amavis, clamav y spamassasin

<div class='ejercicios' markdown='1'>

* **Tarea 6 (3 puntos):** Muestra al profesor el envío y recepción de correos utilizando el webmail.
* **Tarea 7 (5 puntos):** Muestra al profesor el funcionamiento del sistema de filtrado de virus y spam.

</div>

#### En casa

* Configura adecuadamente el router de casa para que el puerto 25/tcp de tu equipo sea accesible desde Internet (eso se denomina DNAT o port forwarding)
* Date de alta en un servidor DNS dinámico como dyndns.org, no-ip.com, etc. o usa el nombre de dominio propio.
* Configura el DNS de tu proveedor para que la máquina a la que apunta el registro MX corresponda a tu IP pública. Si vas a utilizar un servicio gratuito como dyndns.org, no-ip.com, simplemente debes configurarlo para que apunte a tu ip.
* Instala postfix en tu máquina y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.)
* Prueba a enviar desde tu equipo un correo electrónico a josedom24@openmailbox.org , que no lo rechazará aunque venga de una dirección IP dinámica.
* Prueba a enviar desde tu equipo un correo electrónico a hotmail/gmail y comprueba que rebota los mensajes (mira en /var/log/mail.log), ya que no acepta correos de direcciones IP dinámicas.
* Configura postfix para que envíe el correo electrónico a través de gmail como se indica en la documentación. Cuando funcione envía un correo a josedom24@gmail.com

<div class='ejercicios' markdown='1'>

* **Tarea 8 (2 puntos):** Envía el correo a josedom24@openmailbox.org
* **Tarea 9 (3 puntos):** Responde al correo qu yo te voy a mandar desde esa dirección.
* **Tarea 10 (4 puntos):** ¿Te rebota el correo enviado al exterior por qué estas usando ip dínamica? Independientemente de la respuesta, muestra el log donde se vea el envío de ese correo y documenta la configuración del relay con gmail. Finalmente envía un correo a josedom24@gmail.com.

</div>

* En el servidor de clase, configura postfix para que use usuarios virtuales guardados en un servidor ldap.
	* Instala un esquema adecuado para usuarios de postfix en LDAP
	* Crea un script que reciba un nombre de usuario y añade un nuevo registro al LDAP:

	1. El dn debes ajustarlo a la base a la de tu directorio
	2. Cada entrada incluye un objectClass y atributos adecuados para postfix 
	3. El atributo mail es del tipo usuario@dominio
	4. El buzón de cada usuario está en formato Maildir 
	5. El atributo userPassword es un hash SSHA del uid del usuario

<div class='ejercicios' markdown='1'>

* **Tarea 11 (5 puntos):** Documenta en redmine la configuración realizada. Y realiza una prueba de funcionamiento al profesor.

</div>
      
[Volver](index)

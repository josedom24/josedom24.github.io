---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

# Proyecto 4: Configuración de un servidor de correos

Esta tarea consiste en instalar y configurar un servidor de correo similar al de cualquier organización capaz de enviar y recibir directamente correo, almacenar los usuarios en LDAP, filtrar el correo en busca de virus o spam y servirlo a sus usuarios a través de los protocolos POP, IMAP y configurar un Webmail.

### Objetivos

1. Instalar y configurar un servidor postfix en un equipo con dirección IP pública dinámica
2. Aprender a configurar todos los componentes de un servidor de correos completo
3. Depurar el funcionamiento de un servicio
4. Documentar adecuadamente todo el proceso

### Pasos a realizar

#### En casa

1. Configura adecuadamente el router de casa para que el puerto 25/tcp de tu equipo sea accesible desde Internet (eso se denomina DNAT o port forwarding)
2. Date de alta en un servidor DNS dinámico como dyndns.org, no-ip.com, etc. o usa el nombre de dominio propio.
3. Configura el DNS de tu proveedor para que la máquina a la que apunta el registro MX corresponda a tu IP pública. Si vas a utilizar un servicio gratuito como dyndns.org, no-ip.com, simplemente debes configurarlo para que apunte a tu ip.
4. Instala postfix en tu máquina y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.)
5. Prueba a enviar desde tu equipo un correo electrónico a correo@josedomingo.org, que no lo rechazará aunque venga de una dirección IP dinámica.
6. Prueba a enviar desde tu equipo un correo electrónico a hotmail y comprueba que rebota los mensajes (mira en /var/log/mail.log), ya que no acepta correos de direcciones IP dinámicas.
7. Configura postfix para que envíe el correo electrónico a través de gmail como se indica en la documentación. Cuando funcione envía un correo a josedom24@gmail.com

#### En clase

1. Vamos a realizar un sistema de correo para el dominio tudominio.gonzalonazareno.org, cuyo servidor DNS lo administras en la máquina cronos. Tienes que comunicar el nombre de dominio al profesor para configurar el servidor de correos del departamento.
2. Instala postfix en una máquina y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.)
3. Configura tu servidor de correos para que use a babuino como relay.
4. Prueba a enviar desde tu equipo un correo electrónico a correo@josedomingo.org, explica qué ocurre.
5. Prueba a enviar desde tu equipo un correo electrónico a hotmail y comprueba que ocurre.
6. Instala y configura un servidor dovecot POP e IMAP en tu equipo
7. Configura adecuadamente un cliente de correo (evolution, outlook, thunderbird, ...) para que reciba el correo a través de POP o IMAP. El cliente debe estar configurado en una máquina cliente. Instala un servidor DNS en el servidor para que se puedan resolver los nombres de los servidores.
8. Instala y configura correctamente un sistema de filtrado de virus y spam utilizando amavis, clamav y spamassasin
9. Instala un webmail (roundcube) para gestionar el correo del equipo mediante una interfaz web.

##### Parte optativa

1. Instala openLDAP  configurando la base DNS de manera adecuada.
2. Instala un esquema adecuado para usuarios de postfix en LDAP
3.  Crea un script que reciba un nombre de usuario y añade un nuevo registro al LDAP:

* El dn debes ajustarlo a la base a la de tu directorio
* Cada entrada incluye un objectClass y atributos adecuados para postfix 
* El atributo mail es del tipo usuario@dominio
* El buzón de cada usuario está en formato Maildir 
* El atributo userPassword es un hash SSHA del uid del usuario

#### Ficheros a entregar

Sube en la tarea correspondiente un fichero comprimido en formato tgz que incluya:
1. Una memoria completa de la tarea en formato pdf donde se describan con detalle todos los pasos dados y las pruebas de funcionamiento realizadas, incluyendo capturas de pantalla y registros de funcionamiento.
2. Los ficheros de configuración más relevantes
3. Las líneas adecuadas de los ficheros de registros implicados 

      
[Volver](index)

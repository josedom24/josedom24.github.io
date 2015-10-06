---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Configuración de un servidor GNU/Linux

<div class='notas' markdown='1'>

###Objetivo

El objetivo de esta práctica es montar una infraestrucuta de servicios que se mantenga en el tiempo y que nos sirva para montar servicios y aplicaciones en los distintos módulos durante el curso. Esta práctica la tenéis que realizar en la infraestructura de máquinas que hemos creado en el cloud para todas los módulos. En cualquier momento del curso los servicios que instalemos en esta práctica deben estar funcionando de manera adecuada.

</div>

### Servidor DNS

Vamos a instalar un sevidor dns que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor dns con autoridad sobre un subdominio de nuestro dominio principal *gonzalonazareno.org*, que se llamará **tu_nombre**.*gonzalonazareno.org*.

<div class='ejercicios' markdown='1'>

Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal *papion*.

</div>

#### Instalación del servidor DNS

El servidor DNS se va a instalar en el servidor 2. Y en un primer momento se configurará de la siguiente manera:

* El servidor DNS se llama *servidor2.**tu_nombre**.gonzalonazareno.org* y va a ser el servidor con autoridad para la zona **tu_nombre**.*gonzalonazareno.org*.
* El servidor debe resolver el nombre de los tres servidores.
* Se debe configurar la zona de resolución inversa.

<div class='notas' markdown='1'>

* Debes determinar si la resolución directa se hace con dirección ip fijas o flotantes del cloud depediendo del servicio que se este prestando.
* Debes considerar la posibilidad de hacer dos zonas de resolución inversa para resolver ip jijas o flotantes del cloud.
* Debes modificar la configuración del servidor DHCP del cloud para que mande a los servidores el nuevo nombre de dominio.

</div>

<div class='ejercicios' markdown='1'>

* **Tarea 1 (1 puntos):** Comprueba que los servidores tienen configurados el nuevo nombre de dominio de forma adecuada después de volver a renovar la concesión del servidor DHCP. Documenta el contenido del fichero en el que se puede comprobar este punto.
* **Tarea 2 (2 puntos)(Obligatorio):** Entrega el resultado de las siguientes consultas :
	* El servidor DNS con autoridad sobre la zona del dominio **tu_nombre**.*gonzalonazareno.org*
	* La dirección IP de los tres servidores
	* Un resolución inversa
</div>

### Servidor Web

En nuestro servidor1 vamos a instalar un servidor Web apache2 con las siguientes características.

<div class='ejercicios' markdown='1'>

* **Tarea 3 (1 punto)(Obligatorio):** Nuestro servidor va  a tener dos hosts virtuales: www.**tu_nombre**.*gonzalonazareno.org* y informatica.**tu_nombre**.*gonzalonazareno.org*. Explica los pasos fundamentales para realizar los dos virtual hosts.
* **Tarea 4 (1 punto):** Comenta los cambios en el servidor DNS para de dar de alta los dos nuevos nombres.
* **Tarea 5 (1 punto):** La página www.**tu_nombre**.*gonzalonazareno.org* va a ser la página principal, busca una plantilla html, modifícala un poco y desplegala en el primer virtual host. Muestrasela al profesor.
* **Tarea 6 (1 punto):** Por seguridad, en la página www.**tu_nombre**.*gonzalonazareno.org*, no se permite que se sigan enlaces simbólicos, no se permite negociación de contenidos, no se permite visualizar la lista de ficheros y no se permite usar ficheros .htaccess. Entrega la modificaciones en la configuración necesarias.
* **Tarea 7 (1 punto):** La página informatica.**tu_nombre**.*gonzalonazareno.org* es una página relacionada con el mundo de la informática, busca una plantilla html, modifícala un poco y desplegala en el primer virtual host. La págian se guardará en  un directorio llamado plataforma. Por lo tanto si accedemos a informatica.example.com se debererá redirigir automáticamente a informatica.example.com/plataforma. Muestra el resultado al profesor.
* **Tarea 8 (3 puntos):** Para llevar una estadistica de visitas y accesos instala la aplicación awstats en el servidor. Configura el cron para que la estadistíca se vaya actualizando. Debes realizar dos estadísticas, una para cada host virtual.
* **Tarea 9 (2 puntos):**En el directorio /srv/isos tenemos una colección de imágenes isos, queremos acceder a ella en la dirección informatica.**tu_nombre**.*gonzalonazareno.org*/isos. Esta dirección debe ser sólo accesible desde la intranet, si accedemos desde fuera tenemos que autentificarnos (digest) con un usuario.

</div>

[Volver](index)
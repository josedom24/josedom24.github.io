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

* **Tarea 1 (1 puntos):** Comprueba que los servidores tienen bien configurado el nuevo nombre de dominio de forma adecuada después de volver a renovar la concesión del servidor DHCP.


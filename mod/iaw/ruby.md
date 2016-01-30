---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Despliegue de una aplicación Ruby/RoR 

<div class='nota' markdown='1'>

* **Entorno de desarrollo/pruebas**: Máquina virtual (vagrant o cloud)
* **Entorno de producción**: Heroku
* **Método de despliegue**:Capistrano

</div>

<div class='ejercicios' markdown='1'>
Para el despliegue de apalicaciones web Ruby/Ror (octopress,fedena,diaspora,gitlab,redmine,openproject,spree,cartoDB,Publify,Typo,radiantcms,...), podemos escoger entre varios servidores web (apache, nginx,...), varias servidores de aplicaiones ruby (unicorn, Phusion Passenger, Puma, Rainbows, Thin,...) y si es necesario varios gestores de base de datos (MongoDB, PosgreSQL, mysql,...)

Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando la combinación de aplicación web, servidor web, servidor de aplicaciones y base de datos que vas a utilizar. Comenta en la tarea redmine los pasos relevantes que vas realizando.
</div>

Esta tarea consiste en desplegar una aplicación web ruby/RoR, siguiendo los siguientes pasos:

* Crea una instancia de vagrant/cloud basado en debian o ubuntu
* Despliega la aplicación ruby/ror en local.
* Configura un servidor web en local y el servidor de aplicaciones escogido. Realiza la configuración necesaria para que sirva la aplicación web.

<div class='ejercicios' markdown='1'>
En este momento, muestra al profesor la aplicación funcionando en local. 
</div>

* Realiza el despliegue de la aplicación a Heroku.
* Realiza el despliegur utilizando la herramienta Capristano.

<div class='ejercicios' markdown='1'>

* Muestra al profesor la aplicación funcionando en producción.
* Realiza algún cambio en el CMS en el entorno de desarrollo/prueba, y despliega de nuevo al entorno de producción.

</div>
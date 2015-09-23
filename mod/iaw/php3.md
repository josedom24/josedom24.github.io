---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Despliegue de una aplicación web desarrollada en PHP en PaaS
<div class='nota' markdown='1'>

* **Entorno de desarrollo/pruebas**: Máquina local virtual (vagrant) o instancia del cloud
* **Entrono de producción**: PaaS. OpenShift
* **Configuración del entorno**: Manual o automático
* **Método de despliegue**: El ofrecido por OpenShift: git
</div>

<div class='ejercicios' markdown='1'>
Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando qué CMS has elegido. Comenta en la tarea redmine los pasos relevantes que vas realizando.
</div>

Esta tarea consiste en desplegar un CMS de tecnología PHP en PaaS (OpenShift), pero es conveniente no hacer el despliegue directamente en el entorno de producción sino que se seguirá el siguiente procedimiento:* 

* Crea una instancia de vagrant/openstack basado en un box debian o ubuntu
* Instala en esa máquina virtual toda la pila LAMP. Lo puedes hacer manualmente o modificando la receta ansible del ejercicio anterior para realizar la instlación en un solo nodo.
* Accede a OpenShift
* Crea un gear de tipo PHP
* Añade el cartridge MySQL
* Clona el repositorio de OpenShift en la máquina virtual
* Configura la aplicación para que funcione en la máquina virtual

<div class='ejercicios' markdown='1'>
En este momento, muestra al profesor la aplicación funcionando en local.
</div>

* Crea una BBDD local para la aplicación web
* Descarga e instala en local la aplicación web
* Realiza una configuración mínima de la aplicación
* Realiza el despliegue en OpenShift con git
* Verifica el buen funcionamiento de la aplicación en el entorno de PaaS

<div class='ejercicios' markdown='1'>

* Muestra al profesor la aplicación funcionando en producción.
* Realiza algún cambio en el CMS en el entorno de desarrollo/prueba, y despliega de nuevo al entorno de producción.
</div>
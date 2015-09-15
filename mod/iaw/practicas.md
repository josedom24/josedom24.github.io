---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

Esta tarea consiste en desplegar un CMS de tecnología PHP en un hosting compartido, pero es conveniente no hacer el despliegue directamente en el entorno de producción sino que se seguirá el siguiente procedimiento:

    Crea una instancia de vagrant basado en un box debian o ubuntu
    Instala en esa máquina virtual toda la pila LAMP
    Crea una BBDD local para la aplicación web
    Descarga e instala en local la aplicación web
    Realiza una configuración mínima de la aplicación
    Date de alta en un servicio de hosting compartido con soporte para PHP
    Configura adecuadamente todos los parámetros (DNS, usuarios, BBDD, etc.)
    Transfiere los ficheros de la aplicación web desde el entorno de desarrollo utilizando FTP o SSH
    Realiza un volcado de la base de datos local y utilízalo para configurar la base de datos en el entorno de producción
    Verifica el buen funcionamiento de la aplicación en el entorno de hosting compartido

Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando qué CMS has elegido.

Comenta en la tarea los pasos relevantes
<hr/>



Esta tarea consiste en desplegar un CMS de tecnología PHP en PaaS (OpenShift), pero es conveniente no hacer el despliegue directamente en el entorno de producción sino que se seguirá el siguiente procedimiento:

    Accede a OpenShift
    Crea un gear de tipo PHP
    Añade el cartridge MySQL
    Crea una instancia de vagrant basado en un box debian o ubuntu
    Instala en esa máquina virtual toda la pila LAMP
    Clona el repositorio de OpenShift en la máquina virtual
    Configura la aplicación para que funcione en la máquina virtual
    Crea una BBDD local para la aplicación web
    Descarga e instala en local la aplicación web
    Realiza una configuración mínima de la aplicación
    Realiza el despliegue en OpenShift con git
    Verifica el buen funcionamiento de la aplicación en el entorno de PaaS

Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando qué CMS has elegido.

Comenta en la tarea los pasos relevantes

<hr/>



Esta tarea consiste en desplegar una aplicación web Java en una máquina virtual, que podría considerarse un entorno de pruebas.

    Crea una instancia de vagrant basado en un box debian o ubuntu
    Instala JRE 7
    Instala Tomcat
    Instala PostgreSQL
    Elige una aplicación web, instálala en el entorno anterior y configúrala.

Comenta en la tarea los pasos relevantes
<hr/>


Esta tarea consiste en desplegar una aplicación web Java en PaaS (OpenShift), pero es conveniente no hacer el despliegue directamente en el entorno de producción sino que se seguirá el siguiente procedimiento:

    Accede a OpenShift
    Crea un gear de tipo Tomcat-7
    Añade el cartridge PostgreSQL
    Crea una instancia de vagrant basado en un box debian o ubuntu o reutiliza una que tuvieras
    Clona el repositorio de OpenShift en la máquina virtual
    Evalúa si es más adecuado utilizar el tomcat del sistema (instalado mediante apt) o un tomcat instalado en un directorio.
    Instala PostgreSQL-9 en el entorno de pruebas
    Configura la aplicación para que funcione en la máquina virtual
        Crea una BBDD local para la aplicación web
        Descarga e instala en local la aplicación web
        Realiza una configuración mínima de la aplicación
    Realiza el despliegue en OpenShift con git
        Realiza las adaptaciones necesarias para que la aplicación se pueda ejecutar en local y en producción manteniendo la sincronización de git
        Realiza el poblado inicial de la BBDD en OpenShift utilizando un volcado de la base de datos local
    Verifica el buen funcionamiento de la aplicación en el entorno de PaaS

NOTA: Comenta en la tarea los pasos relevantes

<hr/>


Esta tarea consiste en desarrollar una aplicación web sencilla utilizando el framework django. Una de las características de Django es que hay gran cantidad de aplicaciones ya desarrolladas por lo que puedes utilizar todos los componentes adicionales que quieras para añadirle funcionalidad a tu aplicación.

    Haz una pequeña memoria sobre las características de tu aplicación web y entrégala antes del 14 de Enero
    Realiza los pasos necesarios para desarrollar tu aplicación localmente y desplegarla en OpenShift, utilizando un entorno virtual de Python para el desarrollo local
    Añade mi clave pública RSA a OpenShift para tener acceso a la aplicación
    Documenta en esta tarea de forma continua los pasos que vayas realizando, tanto los avances como los errores que vayas encontrando

<hr/>

n esta tarea vamos a ver las características necesarias para desplegar una aplicación web desarrollada en ruby, tanto en un entorno de pruebas como en un entorno en producción.

    Elige una aplicación web desarrollada en Ruby que no haya elegido un compañero
    Elige un entorno de producción para desplegarla (OpenShift, instancia de cloud, hosting, ...)
    Elige una combinación de servidor web y servidor de aplicación ruby para tu entorno de pruebas
    Si utilizas capistrano para el despliegue de la aplicación en producción, la tarea valdrá 6 puntos
    Despliega la aplicación en ambos entornos

Explica en la tarea los pasos relevantes

<hr/>


Con idea de experimentar una primera aproximación al despliegue de aplicaciones web dentro de un contenedor con docker, realiza una práctica en la que se despliegue una aplicación web completa en un contenedor en un determinado entorno y exportala a otro.

Para ello puedes utilizar diferentes técnicas: Imagen completa estática, dockerfile, ansible, etc. Elige la que prefieras y documenta todo el proceso.

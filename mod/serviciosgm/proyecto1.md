---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Proyecto 1: Configuración de un servidor Windows Server

Te han contratado como administrador de redes en una empresa que posee una red de ordenadores con varios clientes 
y un servidor donde se ha instalado un sistema operativo Windows 2008. Actualmente la dirección de la empresa quiere 
mejorar la gestión de la red y ese es tu objetivo. Quieren mejorar los siguientes aspectos de la red:
* Actualmente la configuración de red de los cliente se hacía de forma estática, en un segmento de direcciones 10.0.0.0/24. Quieren tener un sistema de asignación dinámica de direcciones IP.
* Quieren crear varias páginas web para dar servicio a la intranet para ello han contratado un dominio masterlan.com
* Para poder acceder a los distintas máquinas de la intranet, se necesita que instales un servidor DNS.
* Los documentos importantes de la empresa deben ser accesible desde un servidor ftp anónimo.
* Un grupo de usuarios (los técnicos) pueden gestionar el servidor de forma remota.
* Todos los usuarios deben poseer una cuenta de correos de la forma usuario@masterlan.com

#### Esquema de red

El esquema de red que tiene la empresa es el siguiente:

![Esquema de red](img/esquema_red.png)

Como se observa en el esquema nuestro ordenador va a tener dos tarjetas de red, por lo tanto va a ser el
responsable de gestionar la comunicación que entra y sale de nuestra red local.

La primera tarjeta está conectada a internet (en nuestro caso está conectada a la red del instituto), la segunda
tarjeta está conectada a la red local y tiene el siguiente direccionamiento:

* Dirección IP: 10.0.0.1/24

#### Servidor DHCP

Los ordenadores clientes de nuestra LAN obtienen su configuración de red ofrecidas por dicho servidor, que tiene las siguientes características:

* Rango: 10.0.0.2-10.0.0.200
* Máscara de red: 255.255.255.0 
* Puerta de enlace: La ip del router
* DNS: 8.8.8.8

<div class='ejercicios' markdown='1'>
##### **Entrega 1**
1. Escribe una introducción donde expliques el objetivo de la práctica. El esquema real que estás desarrollando y cómo lo vas a virtualizar para poder desarrollarlo en clase. Por último indica el nombre que le has puesto al ordenador servidor. ¿Cómo has configurado ese nombre?
2. Explica la configuración de red del servidor y de los dos clientes
3. Explica la configuración del servidor para que funcione como router y nat
4. Explica la instalación y configuración del servidor DHCP.
5. Prueba de funcionamiento (Concesiones de direcciones)
6. Realiza una reserva de uno de los clientes, explica cómo lo has realizado y haz una prueba de funcionamiento.
</div>

#### Servidor WEB

Se necesitan crear dos páginas webs con las siguientes características:

* La primera se llamará **www.masterlan.com**, su directorio base será *c:/web/principal*. Es la página corporativa de la empresa, y tendrá una zona privada autentificada para los clientes de la empresa.
* La segunda se llamará **direccion.masterlan.com**, su directorio base será *c:/web/privado*. Es la página de trabajo de los trabajadores de la empresa. El acceso a esta página será auntentificada y sólo podrán entrar los trabajadores.


<div class='ejercicios' markdown='1'>
##### **Entrega 2**
1. Crea los usuarios que creas necesarios para hacer la pruebas de autentificación. Del mismo modo crea los grupos que vas a necesitar. Explica el proceso de creación de usuario y grupos.
2. Crea los dos sitios virtuales, explica el proceso de creación de hosts virtuales.
3. Elije una plantilla adecuada, y modifícala de tal manera que aparezca el nombre de la empresa (invéntatelo). En cada página tiene que haber un enlace a la otra página. Y en la primera debe haber un enlace a la zona de clientes.
4. Autentificación de las páginas. Utilizando autentificación básica explica el proceso para que la zona de clientes de la primera página sólo sea accesible por los clientes de la empresa, y que la segunda página sólo sea accesible por los trabajadores.
5. Muestra la modificación de los ficheros hosts para el acceso desde los clientes.
6. Por medio de capturas de pantalla, demuestra como se accede a las distintas páginas.
</div>
[Volver](index)
Modifica el fichero hosts de forma adecuada en los clientes y accede a dichas páginas 

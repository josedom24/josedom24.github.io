---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Instalación y configuración del servidor dhcp en linux usando varios ámbitos

#### Preparación del escenario

Crea un escenario usando Vagrant que defina las siguientes máquinas:

* Servidor: Tiene tres tarjetas de red: una pública y dos privadas que se conectan a dos redes locales.
* nodo_lan1: Un cliente conectado a la primera red local.
* nodo_lan2: Un cliente conectado a la segunda red local.

La dirección de la primera red local será 10.0.1.0/24 y la de la segundo será 10.0.2.0/24.

Una vez levantada las máquinas modifica los clientes para que tomen direccionamiento dinámico.

#### Servidor dhcp

Instala un servidor dhcp en el ordenador "servidor" que reparta direcciones a las dos redes locales.

#### Enrutador y NAT

Configurador el servidor para que funcione como router y haga NAT de esta forma los clientes tendrán internet.

<div class='ejercicios' markdown='1'>
### Para entregar...
1. Entrega el fichero Vagrantfile 
2. Entrega un pequeño manual donde expliques como has configurado el servidor dhcp.
3. Realiza comprobaciones del funcionamiento (con salidas de los comandos ifconfig y contenido del fichero de concesión.
4. Explica con detalle cómo has configurado el servidor para que funcione como router - nat.
</div>
[Volver](index)

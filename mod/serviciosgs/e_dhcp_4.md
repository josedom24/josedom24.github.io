---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Ejercicio completo del servidor dhcp

#### Preparación del escenario

Crea un escenario usando Vagrant que defina las siguientes máquinas:

* Servidor: Tiene tres tarjetas de red: una pública y dos privadas que se conectan a dos redes locales.
* nodo_lan1: Un cliente conectado a una red local.

#### Servidor dhcp

Instala un servidor dhcp en el ordenador "servidor" que de servicio a los orednadores de red local, teniendo en cuante que le tiempo de consesión sea 12 horas y que la red local tiene el direccionamiento 192.168.100.0/24.

<div class='ejercicios' markdown='1'>
### Ejercicios 
1. Entrega el fichero Vagrantfile que define el escenario.
2. Explica las modificaciones que has hecho en los distintos ficheros de configuración.
3. Explica la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
</div>

#### Funcionamiento del dhcp

<div class='ejercicios' markdown='1'>
### Realiza las siguientes comprobaciones
Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstacia, para ello vamos a poner un tiempo de conseción muy bajo.

1. Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
2. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?

</div>

#### Reservas

Crea una reserva para el que el cliente tome siempre la dirección 192.168.100.100.

<div class='ejercicios' markdown='1'>
1. Indica las modificaciones realizadas en los ficheros de configuración y entrega una comprobación de que el cliente ha tomado esa dirección.
</div>

#### Uso de varios ámbitos

Modifica el escenario Vagrant para añadir una nueva red local y un nuevo nodo:

* nodo_lan2: Un cliente conectado a la segunda red local.

Instala un servidor dhcp en el ordenador "servidor" que de servicio a los orednadores de red local, teniendo en cuante que le tiempo de consesión sea 24 horas y que la red local tiene el direccionamiento 192.168.200.0/24.

<div class='ejercicios' markdown='1'>
### Ejercicios 
1. Entrega elnuevo fichero Vagrantfile que define el escenario.
2. Explica las modificaciones que has hecho en los distintos ficheros de configuración.
3. Explica la configuración que has hecho en el segundo cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
</div>

#### Enrutador y NAT

Configurador el servidor para que funcione como router y haga NAT de esta forma los clientes tendrán internet.

<div class='ejercicios' markdown='1'>
### Para entregar...
1. Entrega una comprobación de que los clientes tienen internet.
</div>

#### Script

Realiza un script en python que de información de las conseciones del servidor:

infodhcp.py -l: Nos muestra todas las ips que están concedidadas (las reservas también). Nos da información de los dos ámbitos.
infodhcp.py x.x.x.x : Nos dice si esa ip está concedida y que MAC corresponde.

<div class='ejercicios' markdown='1'>
### Para entregar...
1. Entrega la URL del repositorio GitHub donde tienes el programa
</div>


[Volver](index)

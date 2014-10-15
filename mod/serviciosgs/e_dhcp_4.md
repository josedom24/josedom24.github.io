---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Ejercicio completo del servidor dhcp

#### Teoria

<div class='ejercicios' markdown='1'>
##### Ejercicios 
1. Lee el documento [Teoría: Servidor DHCP](http://dit.gonzalonazareno.org/moodle/mod/resource/view.php?id=1868) y explica el funcionamiento del servidor DHCP resumido en este [gráfico](img/dhcp.png).
</div>

#### Preparación del escenario

Crea un escenario usando Vagrant que defina las siguientes máquinas:

* Servidor: Tiene dos tarjetas de red: una pública y una privadas que se conectan a la red local.
* nodo_lan1: Un cliente conectado a la red local.

#### Servidor dhcp

Instala un servidor dhcp en el ordenador "servidor" que de servicio a los ordenadores de red local, teniendo en cuanta que el tiempo de concesión sea 12 horas y que la red local tiene el direccionamiento 192.168.100.0/24.

<div class='ejercicios' markdown='1'>
##### Ejercicios 
1. Entrega el fichero Vagrantfile que define el escenario.
2. Explica las modificaciones que has hecho en los distintos ficheros de configuración del servidor.
3. Explica la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
4. Configura el servidor para que funcione como router y haga NAT de esta forma los clientes tendrán internet.
5. Realizar una captura, desde el cliente usando **tcpdump**, de los cuatro paquetes que corresponden a una concesión: DISCOVER, OFFER, REQUEST, ACK.
</div>

#### Funcionamiento del dhcp

<div class='ejercicios' markdown='1'>
##### Realiza las siguientes comprobaciones
Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstacias, para ello vamos a poner un tiempo de concecsión muy bajo.

1. Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
2. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?

</div>

#### Reservas

Crea una reserva para el que el cliente tome siempre la dirección 192.168.100.100.

<div class='ejercicios' markdown='1'>
##### Ejercicios 
1. Indica las modificaciones realizadas en los ficheros de configuración y entrega una comprobación de que el cliente ha tomado esa dirección.
</div>

#### Uso de varios ámbitos

Modifica el escenario Vagrant para añadir una nueva red local y un nuevo nodo:

* Servidor: En el servidor hay que crear una nueva interfaz
* nodo_lan2: Un cliente conectado a la segunda red local.

Configura el servidor dhcp en el ordenador "servidor" para que de servicio a los ordenadores de la nueva red local, teniendo en cuante que el tiempo de concesión sea 24 horas y que la red local tiene el direccionamiento 192.168.200.0/24.

<div class='ejercicios' markdown='1'>
##### Ejercicios 
1. Entrega el nuevo fichero Vagrantfile que define el escenario.
2. Explica las modificaciones que has hecho en los distintos ficheros de configuración.
3. Explica la configuración que has hecho en el segundo cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
</div>

#### Script

Realiza un script en python que de información de las concesiones del servidor:

infodhcp.py -l: Nos muestra todas las ips que están concedidas (las reservas también). Nos da información de los dos ámbitos.
infodhcp.py x.x.x.x : Nos dice si esa ip está concedida y a que MAC corresponde.

<div class='ejercicios' markdown='1'>
##### Para entregar...
1. Entrega la URL del repositorio GitHub donde tienes el programa
</div>


[Volver](index)

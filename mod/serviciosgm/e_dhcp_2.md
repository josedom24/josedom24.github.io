---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de un servidor DHCP en Windows Server 2008 (2)

En nuestra red interna es necesario, por diversas razones, cambiar el direccionamiento de red. Necesitamos implantar un red 10.0.0.0/8:
Pasos a seguir:

#### Configuración de la red

Cambia la dirección estática de la red interna del servidor Windows y ponle la siguiente configuración:

* Dirección IP: 10.0.0.1
* Mascara de red: 255.0.0.0


#### Configuración del servidor DHCP

Modifica la configuración del servidor DHCP con los siguientes datos:

* Ámbito: iesgn
* Rango de direcciones a repartir: 10.0.0.10 - 10.0.0.20
* Máscara de red: 255.0.0.0
* Duración de la concesión: 1 hora
* Puerta de enlace: 10.0.0.1
* Servidores DNS: **208.67.222.222,  208.67.220.220**
* Sin servidores WINS

#### Configura los clientes

Renueva la concesión en los clientes y si es necesario, modifica la configuración del enrutador en el servidor Windows para darle internet a los clientes.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1. Comprueba en las propiedades del servidor DHCP que has realizado la configuración adecuada.
2. Comprueba las concesiones de direcciones que has realizado.
3. Comprueba en cada uno de los clientes la configuración que han tomado.
</div>
[Volver](index)


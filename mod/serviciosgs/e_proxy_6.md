---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Configuración de parámetros de proxy en clientes web

#### Configuración manual de parámetros de proxy

En los navegadores web ya sabemos configurar manualmente el proxy. En este ejercicio configura un máuina virtual, sin entorno gráfico, para que al navegar con lynx se este usando el proxy.

#### Configuración de parámetros de proxy usando script Proxy Auto-config

Configura un servidor web apache2 para que sirva un fichero proxy.pac. Crea dicho fichero con la configuración básica del proxy, e indica las siguientes exclusiones: no se usa el proxy cuando se accede al dominio gonzalonazareno.org y no se usa el proxy cuando se accede a localhost.

Configura el cliente web en la opción: *Configuración automática de proxy*

#### Configuración de parámetros de proxy usando la detección automática WPAD

Configura un servidor bind9 que permita a los clientes con direccionamiento estático encontrar la configuración del proxy.

#### Proxy transparente

En el esquema de red de clase (kvm):

        iptables -t nat -A PREROUTING ! -s 10.0.0.1 -i virbr1 -p tcp --dport 80 -j DNAT --to 10.0.0.1:3128

En el esquema router+nat+proxy:

        iptables -t nat -A PREROUTING  -s 10.0.0.0/24 -i virbr1 -p tcp --dport 80 -j REDIRECT --to-port 3128





[Volver](index)

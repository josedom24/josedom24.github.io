---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Configuración de parámetros de proxy en clientes web

####Configuración manual de parámetros de proxy

En los navegadores web ya sabe,os configurar manualmente el proxy. En este ejercicio configura patricio (sin entorno gráfico) para que al navegar con lynx se este usando el proxy.

####Configuración de parámetros de proxy usando script Proxy Auto-config

Configura el servidor web apache2 en bbobesponja para que sirva un fichero proxy.pac. Crea dicho fichro con la configuración básica del proxy, e indica las siguientes exclusiones: no se usa el proxy cuando se accede al dominio gonzalonazareno.org y no se usa el proxy cuando se accede a localhost.

Configura el cliente web en la opción: *Configuración automática de proxy*

####Configuración de parámetros de proxy usando la detección automática WPAD

1. Configura un servidor dhcp en bobesponja que permita que los clientes al recibir la configuración dinámica configuren los parámtros de acceso al proxy.
2. Configura el servidor bind9 en bobesponja que permita a los clientes con direccionamiento estático encontrar la configuración del proxy.

####Proxy transparente

En el esquema de red de clase:

        iptables -t nat -A PREROUTING ! -s 10.0.0.1 -i virbr1 -p tcp --dport 80 -j DNAT --to 10.0.0.1:3128

En el esquema router+nat+proxy:

        iptables -t nat -A PREROUTING  -s 10.0.0.0/24 -i virbr1 -p tcp --dport 80 -j REDIRECT --to-port 3128





[Volver](index)

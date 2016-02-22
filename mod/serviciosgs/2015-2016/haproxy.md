---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Balanceo de carga en servidores Apache con HAproxy

En primer lugar, construye con KVM con vagrant la siguiente infraestructura:

[![haproxy](haproxy2.jpg)](haproxy.jpg)

Ajustar la configuración de las dos máquinas del cluster de balanceo (apache1 y apache2)

1. Deshabilitar la opción KeepAlive en el fichero de configuración /etc/apache2/apache2.conf para realizar la evaluación del rendimiento sin la opción de reutilización de conexiones.

   	    apache1:~# nano /etc/apache2/apache2.conf  
   	       ...
   	       KeepAlive Off
   	       ...

   	    apache2:~# nano /etc/apache2/apache2.conf  
   	       ...
   	       KeepAlive Off
   	       ...

    Nota: este ajuste no es estrictemente necesario (y sería desaconsejable en un entorno de producción real), pero facilita las pruebas manaueles dado que permite detectar inmediatamente el ''cambio'' de destino resultado del balanceo de carga manteniendo la opción por defecto, en las pruebas manuales desde el navegador sería necesario esperar 5 segundos (el time out de keep alive) antes de recargar la página y ver el efecto del reparto de carga

2. Editar los archivos del sitio web para incluir una indicación del servidor real que está sirviendo una petición, de modo que sea posible ''diferenciarlos'' en las pruebas manuales con el navegador 
		
	En apache1

		apache1:~# nano /var/www/html/index.html
		...
		<h1> Servidor por APACHE_UNO </h1>
		...
		apache1:~# nano /var/www/html/sesion.php	
		...
		<h1> Servidor por la máquina APACHE_UNO </h1>
		...

    En apache2	

		apache2:~# nano /var/www/html/index.html
		...
		<h1> Servidor por APACHE_DOS </h1>
		...		

		apache2:~# nano /var/www/html/sesion.php	
		...
		<h1> Servidor por la máquina APACHE_DOS </h1>
		...

    Nota: este ajuste es simplemente una herramienta de depuración en una "granja" de servidores real este comportamiento no tendría sentido, dado que, obviamente, todos los nodos servirían el mismo contenido/aplicaciones

3. Crear en ambas máquinas (apache1, apache2) el script PHP sleep.php:
    
	    apache1~:# nano /var/www/html/sleep.php

		<html>      
			<title> Retardos de x segundos </title>
		<body>
			<h1> Prueba con retardo de x segundos </h1>
			<p> hora de inicio: <?php echo date('h:i:s'); ?> </p>
			<?php  
			for ($i=0; $i < 2000000; $i++) {    
				$str1 = sha1(rand()*rand());  
				$str2 = sha1(rand()*rand());  
				$str3 = sha1($str1+$str2);    
			}
			?>
			<p> hora de fin: <?php echo date('h:i:s'); ?> </p>
		</body>
		</html>

    Comprobación

    	apache1~:# php /var/www/html/sleep.php
	    apache2~:# php /var/www/html/sleep.php



#### Evaluar rendimiento de un servidor Apache sin balanceo

Se realizarán varias pruebas de carga sobre el servidor Apache ubicado en la máquina apache1. Pasos a realizar:

1. Habilitar en **balanceador** la redirección de puertos para que sea accesible el servidor Apache de la máquina apache1 [10.10.10.11] empleando el siguiente comando iptables

	    balanceador:~# echo 1 > /proc/sys/net/ipv4/ip_forward
	    balanceador:~# iptables -t nat -A PREROUTING \
	                            --in-interface eth0 --protocol tcp --dport 80 \
	                            -j DNAT --to-destination 10.10.10.11

Nota: la regla iptables establece una redirección del puerto 80 de la máquina balanceador al mismo puerto de la máquina apache1 para el tráfico procedente de la red externa (interfaz de entrada eth0).




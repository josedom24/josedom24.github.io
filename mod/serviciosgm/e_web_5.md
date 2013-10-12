---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Acceso a un sitio web desde internet


1) Siguiendo la guía anterior "Gestión de DNS externo", crea un nombre de dominio (por ejemplo *tunombre.dyndns-web.com*) apuntando a la dirección IP pública de tu router.

2) Crea en el IIS un sitio web que se llame igual con una pequeña página index.html dando la bienvenida.

3) Accede a la configuración de tu router y redirecciona todo las peticiones al puerto 80 a la ip privada de tu servidor windows 2008.

> En nuestro caso sólo queremos que esté accesible en principio el servidor web, por lo que deberemos configurar el router para que las peticiones que lleguen con destino el puerto 80/tcp se pasen a avatar.

[Volver](index)

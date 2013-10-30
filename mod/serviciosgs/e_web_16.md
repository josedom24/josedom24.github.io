---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Analizador de logs - awstats

Vamos a instalar y configurar un analizador de logs de apache2 que nos permita generar estadísticas de acceso a nuestro servidor web. Hay muchos programas que ofrecen esta funcionalidad pero nosotros vamos a optar por *awstats*. Puedes seguir la [documentación oficial](http://awstats.sourceforge.net/docs/awstats_setup.html) para realizar la instalación y la configuración.

Tienes que tener en cuenta los siguientes puntos:

1. Vamos a trabajar con un sólo host virtual (por ejemplo el default).
2. El acceso a la estadística se hará en la URL *http://nobredelservidor/estadistica*)
3. El acceso a la estadística desde la red local está permitido, si hace desde fuera, por ejemplo desde el host, se requiere autentificación tipo digest (realizar este punto por medio de un fichero .htaccess)
4. Modifica el cron de awstats para que se genere las estadísticas cada 2 minutos.
 
Además de una pequeña guía de los pasos que has dado para la configuración de awstats, entrega una captura de pantalla donde se vea funcionando y alguna prueba de funcionamiento que permita comprobar si funciona el punto 3. 

[Volver](index)

---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

# Proyecto 3: Instalación de un servidor en un centro educativo (Continuación)

Algunos meses después de nuestro despliegue de un servidor en un centro educativo, el director te ha llamado y te ha comentado, que están teniendo problemas con el ancho de banda contratado y que internet va muy lento, además te comenta que les gustaría poder controlar las páginas a los que los alumnos tienen accesos, y tu respuesta es rápida: "Calamar".

Nos han pedido la configuración de un proxy/cache/filtro de contenido en un servidor de una red local en un instituto de educación. Hemos elegido como proxy/cache squid3, y como filtro de contenido dansguardian. Tenemos que tener en cuenta las siguientes consideraciones:

1) El proxy/cache sólo admite conexiones de la red local.

2) Tenemos dos clases de usuarios: profesores y alumnos.

3) Todos los profesores acceden al proxy con un solo nombre de usuario (profesor) y una única contraseña (pass_profe).

4) Todos los alumnos acceden al proxy con un solo nombre de usuario (alumno) y una única contraseña (pass_alum).

5). Se deniega cualquier conexión que no este autentificada con alguno de estos usuarios.

6). Se quieren limitar las siguientes conexiones:

* Para los profesores y alumnos:
   * No se pueden bajar ficheros que se puedan instalar (exe,msi,rar,zip,bin,iso).
   * No tienen acceso a internet los fines de semana.
* Para los alumnos:
   * No pueden ver contenido multimedia.
   * Sólo tienen conexión de 8:00 h. a 14:00 h.

7) El control de las páginas permitidas se hará mediante listas negras usando squid.

8) Vamos a realizar un script en python/bash que funcione de la siguiente manera:

        filtrar.sh -opciones -tipo contenido

Siendo -opciones: -a: añadir, -d: borrar; -tipo: -url: expresa una url, -dom: expresa un dominio; contenido la url o el dominio        que queremos añadir o borrar de la lista negra.

9) Los navegadores de los clientes deben terner configurado el proxy de manera automática, indicando en la URL el fichero de configuración PAC: wpad.nombrededominio.com/wpad.dat, si no se tiene este fichero configurado no se debe tener acceso a internet.

10) En el fichero pac hay que configurar que el acceso al dominio dominio.com no pase por el proxy.

11) Por último tendremos instalado un programa para monitorizar el uso del proxy: sarg. Para visualizar la información generada por dicho programa accederemos a una página web llamada proxy.iesgn.com que sólo será accesible si ponemos el nombre de usuario y la contraseña de los profesores.

###Posible mejora

Realizar el punto 7 y 8 usando el filtro de contenidos dansguardian. Es decir, las listas negras estarán gestionada por dansguardian. Al script filtrar.sh se le añade un nuevo -tipo: -palabra que permite gestionar las lista de palabras prohibidas. Tendrás que pensar que cambios tienes que hacer en el fichero pac.

      
[Volver](index)

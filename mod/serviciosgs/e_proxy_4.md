---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Configuración de los esquemas de control de acceso

Crea diferentes ACL para obtener los siguientes resultados:

#### Reglas de acceso basadas en direcciones IP

1) Sólo permitir el acceso a squid desde la 10.0.0.2.

2) Sólo permitir el acceso en un rango de direcciones (10.0.0.2-10.0.0.4)

3) Permitir el acceso a la red 10.0.0.0

4) No permitir el acceso a las direcciones IP que tenemos listadas en el fichero ip_sin_internet.txt

5) Permitir el acceso a la red 10.0.0.0, excluyendo al rango 10.0.0.10-10.0.0.20

#### Reglas de acceso basadas en puertos, dominios, URLs y tipos MIME

6) Comprueba el acl que viene en el fichero de configuración donde se indican los puertos permitidos.

7) Explica que conseguimos con las siguientes ACL:

        acl Safe_ports port 80 21 443 563 70 210 1025-65535
        acl SSL_ports port 443
        acl CONNECT method CONNECT
        ...
        ...
        ...
        http_access deny !Safe_ports
        http_access deny CONNECT !SSL_ports

8) Evita que nos podamos conectar al dominio youtube.com y todos sus subdominios.

9) Evita que nos podamos conectar a los dominios listados en el fichero url_prohibidas.txt (lista negra)

10) Permite sólo la navegación a un conjuntos de nombres de dominios. (lista blanca)

11) Deniega el acceso a toda URL que contenga la palabra "informatica" (no tener en cuenta mayusculas y minusculas)

12) Deniega el acceso a toda URL que contenga las plabras "betis" o "sevilla"

13) Utilizando las ACL de tipo urlpath_regex, impide el acceso a ficheros pdf.

14) Usando el tipo MIME: evita el acceso a los ficheros de CSS (text/css), a los jpg (image/jpeg)

15) Evita la visualización de los contenidos flash

#### Otras reglas de acceso

16) Evita que se pueda navegar con el navgador Internet Explorer

17) Permite la navegación sólo los días entre semana de 8:00 de la mañana a las 14:00 de la tarde.

[Volver](index)

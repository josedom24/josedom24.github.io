---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Implantación de aplicaciones con docker

#### Ejercicio 1:

* Elige una imagen docker como base para crear un contenedor interactivo. Accede a él y realiza la instalación de un CMS. recuerda que debes crear un script que te permita posteriormente arrancar los servicios necesarios.
* Crea una nueva imagen a partir del contenedor anterior.
* A partir de la nueva imagen crea un contenedor y comprueba que el gestor de contenidos esté funcionando.
* Suponiendo que has instalado docker en tu entrono de desarrollo/prueba, realiza un despliegue del contenedor a un entorno de producción (otra máquina con docker instalado). Para ello guarda la imagen generada en docker hub y bájala en el entorno de producción, para crear un nuevo contenedor.


#### Ejercicio 2:

* Utilizando imágenes de docker hub, crea una infraestructura de contenedores donde instales un gestor de contenido (que no sea wordpress).
* La infraestructura de contenedores debe tener al menos dos contenedores, uno con el servidor web y la aplicación y otro con la base de datos.

#### Ejercicio 3:

* Define un fichero Dockerfile que te permita generar una nueva imagen que permita la creación de nuevos contenedor con un CMS instalado (que no sea wordpress).
* Construye directamente la imagen en docker hub, utilizando como contexto un repositorio github.
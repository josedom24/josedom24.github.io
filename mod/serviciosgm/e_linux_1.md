---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación de paquetes

#### Instalar paquetes

Vamos a instalar un servicio de ejemplo, utilizando la herramienta apt-get. El servicio que vamos a instalar es ntp, que nos permite la sincronización del reloj del sistema.

Para ello vamos a utilizar la instrucción:

        apt-get install ntp

        Leyendo lista de paquetes... Hecho
        Creando árbol de dependencias       
        Leyendo la información de estado... Hecho
        Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
          libmozjs24d xulrunner-24.0
        Use 'apt-get autoremove' to remove them.
        Se instalarán los siguientes paquetes extras:
          libopts25
        Paquetes sugeridos:
          ntp-doc
        Se instalarán los siguientes paquetes NUEVOS:
          libopts25 ntp
        0 actualizados, 2 se instalarán, 0 para eliminar y 13 no actualizados.
        Necesito descargar 635 kB de archivos.
        Se utilizarán 1.460 kB de espacio de disco adicional después de esta operación.
        ¿Desea continuar [S/n]? 

Veamos algunos conceptos antes de contestar:

* ¿Qué son los paquetes extras? Son las dependencias, los paquetes necesarios para que funcione el paquete que queremos usar.
* ¿Qué son los paquetes sugeridos? Son paquetes relacionados con el que queremos instalar y que ofrecen alguna funcionalidad extra.

La herramienta apt-get descarga de los repositorios los paquetes necesarios y utilizando dpkg los instala y configura. Una vez concluida la instalación el servicio ntp estará funcionando.

<div class='nota' markdown='1'>
Antes de realizar el siguiente ejercicio, desinstala el servidor ssh.
</div>

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1) Instala ahora otro servidor que vamos a utilizar durante el curso: el SSH, que nos permite la conexión remota de forma segura a nuestro ordenador.
</div>

#### Desinstalar paquetes:

La opción de apt-get que debemos usar para desisntalar nuestro paquete es la siguiente:

        apt-get remove ntp

Esta opción no elimina los ficheros de configuración del servicio, para hacerlo tenemos que usar la siguiente opción:

        apt-get remove --purge ntp

**Atención!!!: Cuando desinstalamos un paquete, ¿se desinstalan las dependencias?**

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
2) Desinstala el servidor SSH con *apt-get remove*. Comprueba que no se han borrado los ficheros de configuración. (Los ficheros de configuración están en /etc/ssh)

3) Vuelve instalarlo, y desinstala ahora utilizando la opción purge. Comprueba que todos los ficheros relacionados se han borrado.

4) Vuelve a instalar el servidor SSH, ya que lo vamos a utilizar durante el curso. ¿Por qué a partir de la segunda instalación el proceso es más rápido?
</div>

#### Actualizando los paquetes de nuestro sistema

        apt-get update

Para actualizar la lista de paquetes disponibles con la información del fichero /etc/apt/sources.list

        apt-get upgrade

Con esta instrucción actualizamos la instalación de los paquetes a su última versión sin tener en cuenta las dependencias.

        apt-get dist-upgrade 

Con esta instrucción actualizamos la instalación de los paquetes a su última versión pero teniendo en cuenta las dependencias.

Algunas consideraciones:

1. Si estamos trabajando en la rama estable (wheezy) las dependencias de los paquetes no cambian por lo que es lo mismo usar un upgrade que un dist-upgrade.
2. En la versión testing las dependencias pueden ir cambiando por lo que si utilizamos upgrade los paquetes cuyas dependencias han cambiado se retienen y no se actualizan, por lo que es conveniente usar el dist-upgrade para ir resolviendo las dependencias.
Cuando usamos APT para instalar paquetes hace dos tareas por separado: en un primer paso descarga de los repositorios los paquetes que va a instalar, para a continuación usar la instrucción dpkg para desempaquetar y configurar cada paquete. Veamos algunas cuestiones relacionadas con estas dos tares.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
5) Escribe la instrucción qie permite actualizar la lista de paquetes disponibles para instalar.
</div>

#### Descarga de los paquetes para su instalación

Todos los paquetes descargados por APT se almacenan en un directorio, para posteriormente poder instalarlo con dpkg. El directorio donde podemos encontrar los paquetes bajados es:

        /var/cache/apt/archives


Para borrar esta cache de paquetes podemos usar la opción siguiente de APT:

        apt-get clean

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
6) Comprueba los paquetes deb que tienes en tu cache de paquetes.

7) ¿Qué ocurre si desinstala un paquete y lo vuelves a instalar, si el paquete está en la cache?

8) Borra la cache de paquetes y comprueba que se han borrado. Te en cuenta que a continuación deberás instalar algún paquete para tener paquetes en la cache y seguir haciendo las tareas.

</div>

#### Buscando paquetes en los repositorios: apt-cache

Con la siguiente instrucciones podemos buscar paquetes en los repositorios:

        apt-cache search <busqueda>

Busca todos los paquetes que tengan relaciones con las palabras que hayas indicado en la busqueda.

        apt-cache show <paquete>

Te da información del paquete indicado, si tienes instalado el paquete te da información del instalado y de la nueva versión.

        apt-cache showpkg <paquete> 

Te da información más detallada del paquete indicado.

        apt-cache depends <paquete> 

Te da la lista de dependencias del paquete indicado.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

9) Busca todos lo paquetes que tengan la palabra "apache2"

10) Obtén información del paquete ssh que hemos instalado

11) Lista los paquetes de los que depende el paquete phpmyadmin

</div>

#### Aptitude

Siguiendo algún manual de Aptitude realiza las siguientes tareas:

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

12) Busca paquetes que tengan la palabra "ldap"

13) Desinstala el paquete "ssh" que habíamos instalado anteriormente.

14) Instala de nuevo el paquete "ssh".

15) ¿Cuál es la diferencia más importante entre usar aptitude y apt?

</div>
[Volver](index)


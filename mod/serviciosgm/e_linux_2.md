---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Niveles de ejecución. Arranque y parada de los servicios

### Niveles de ejecución

Los niveles de ejecución ( Run Levels ) definen diferentes estados de funcionamiento de un Sistema Linux.

        0 Parada del sistema
        1 Modo monousuario
        2 Modo multiusuario
        3 Modo multiusuario
        4 No usado
        5 Modo multiusuario
        6 Parada y arranque
        7-9 No se usan

#### Secuencia de arranque
**1) Debian arranca ejecutando el programa init. El archivo de configuración de init es /etc/inittab.**

La entrada initdefault determina el nivel de ejecución inicial del sistema.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
1) Edita el fichero **/etc/inittab**, localiza la entrada initdefault, y determina en que nivel de ejecución está trabajando el sistema.

2) También puedes obtener el nivel de ejecución actual ejecutando la instrucción **runlevel**.

</div>

**2) Los primeros scripts que se ejecutan a continuación (indicado en la linea del fichero /etc/inittab: si::sysinit:/etc/init.d/rcS) son los que se encuentra en el directorio /etc/rcS.**

Estos scripts son los encargados de realizar algunas tareas como:

* Monta el file system root y /proc.
* Elimina temporales y archivos de bloqueo.
* Establece el reloj
* Inicia scripts de red y activa la partición swap.
* Activa el teclado y fuentes.
* Carga módulos.
* Establece valores a muchas variables del entorno:PATH, HOSTNAME,...
* Arranca la swap
* Arranca fsck automático, si hace falta.
* Activa quotas.
* Chequea los argumentos pasados al kernel.
* Chequea los filesystems
* Inicializa los puertos serie.
* Puertos USB.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
3) Lista los ficheros que se encuentran en el directorio **/etc/rcS.d**

4) Comprueba que son enlaces simbólicos a los scripts que se encuentran en el directorio **/etc/init.d**
</div>


**3) A continuación se ejecutan los scripts de inicialización de los servicios del nivel de ejecución por defecto.**

Estos scripts se encuentran en los directorios /etc/rcn donde n es el nivel de ejecución.

Ejemplo:

        Nivel Script Directorio
        0      rc 0  /etc/rc0.d/
        1      rc 1  /etc/rc1.d/
        2      rc 2  /etc/rc2.d/
        3      rc 3  /etc/rc3.d/

Es el script **/etc/init.d/rc** el que procesa todos los archivos K y S de los directorios /etc/rcn.d

* Para ( con el argumento stop ) aquellos procesos que comienzan por K ( kill )
* Lanza ( con el argumento start ) los que comienzan por S ( start ).
* Después de la letra S o K hay dos dígitos numéricos que indican el orden de ejecución. El orden es ASCII.
* Todos los ficheros K o S son enlaces simbólicos a los scrips de cada servicio que están en el directorio /etc/init.d

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

5) Visualiza los ficheros de los distintos directorios /etc/rc*n*.d.

6) Comprueba los ficheros de ejecución del nivel de ejecución que se ejecuta por defecto en Debian.

7) Con la instrucción telinit podemos ejecutar otros niveles de ejecución. Entra en el nivel monousuario. Entra en el nivel de reinicio. Entra en el nivel de parada del sistema.
</div>

De modo esquemático podemos ver:

![niveles](img/niveles.png)

**4) ¿Qué hacer para eliminar un servicio en un determinado nivel?**

* Borrar el vínculo simbólico en /etc/rcn.d/
* Renombrarlo con algo que no empiece con S o K y dejarlo por si queremos luego activarlo.
* Lo que no hay que hacer nunca es eliminar el archivo original en /etc/init.d/

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

8) Vamos a eliminar el servicio gdm3 (encargado de iniciar el servidor gráfico) del nivel de ejecución 2, para ello elimina el fichero que inicia ese servicio.

9) Reinica el sistema y comprueba que el servidor gráfico no se ha iniciado.

10) Para restablecer el enlace simbólico para que podamos iniciar el servicio usamos la instrucción update-rc.d (busca la página del manual para aprender más sobre esta instrucción. Ejecuta:

**update-rc.d gdm defaults** para crear los enlaces simbólicos que ejecutan el script de gdm

11) Vuelve a reiniciar el sistema y comprueba que el servidor gráfico se vuelve a ejecutar.

12) Pregunta: ¿Para qué podríamos utilizar la configuración de distintos niveles de ejecución?

</div>

### Arranque y parada de lo servicios

Una vez que se han cargado los servicios que se encuentran en el directorio /etc/rc2.d, podemos comprobar que los demonios correspondientes a cada servicio se están ejecutando con la instrucción:

        ps -A

En cualquier momento podemos parar o reiniciar cualquier servicio ejecutando los scripts del directorio /etc/init.d con las siguientes opciones: start, stop, restart, force-reload,...

También se puede utilizar el comando **service**, de esta forma para reiniciar el servicio ssh podemos ejecutar dos camoandos:

        /etc/init.d/ssh restart
        service ssh restart

<div class='ejercicios' markdown='1'>
##### **Ejercicios**
13) Comprueba que el servicio ssh se está ejecutando.

14) Para el servicio, y comprueba con la instrucción ps que el proceso no se está ejecutando.

15) Vuelve a reiniciar el servicio.

</div>


### Envío de señales a los procesos

Es posible el envío de distintas señales a los procesos. La más usada es matar un proceso, si por ejemplo se queda inactivo. Para ello utilizamos la siguiente instrucción:

        kill -9 PID

El PID es el identificador del proceso, y lo puedes obtener mirando la lista de procesos por ejemplo con ps -A.

Podemos también utilizar la siguiente instrucción

        killall nombredelproceso

Del mismo modo puedes ver el nombre del proceso mirando la lista de procesos con ps.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

16) Imagínate que el servidor gráfico se queda "colgado". Entra en un terminal de texto con CTRL+ALT+F1, y tras iniciar sesión como root mata el proceso gdm (Gestor de arranque del servidor gráfico).

17) Para comprobar que el servidor gráfico no funciona puedes hacer varias cosas: lista los procesos y comprueba que no existe el proceso gdm ni el Xorg. También puedes intentar entrar en la consola gráfica con CTRL+ALT+F7.

18) Vuelve a ejecutar el gestor de arranque gráfico gdm.

19) Del mismo modo puedes matar el demonio del servicio ssh, y volver a reiniciarlo posteriormente.

</div>

### Systemd

Iniciar servicio:

        systemctl start *servicio*

Parar servicio:

        systemctl stop *servicio*

Reiniciar servicio:

        systemctl restart *servicio*

Recargar servicio (si lo permite):

        systemctl reload *servicio*

### Logs de procesos

Los logs de los procesos se guardan en el directorio */var/log/*, por ejemplo el fichero *syslog* es el principal, y en él podemos encontrar mensa      jes de distintos procesos (por ejemplo el servidor dhcp). Algunos servicios tienen su propio fichero de log, por ejemlo */var/log/apache2/error.log*.

Normalmente para ver la últimas líneas del fichero de log, utilizamos el siguiente comando:

        tailf /var/log/syslog

Con systemd tenemos otra manera de ver los logs, si al iniciar un servicio nos da un error, podemos ver los mensajes del log con la instrucción:

        journalctl -xn


<div class='ejercicios' markdown='1'>
##### **Ejercicios**

20) Para el servicio ssh, con systemd.

21) Modifica el fichero de configuración del servidor */etc/ssh/sshd_config*, borra alguna letra para que se produzca un error al inciar el servicio. Inicia el servidor con systemd y comprueba que hay un error.

22) Ejecuta la instrucción adecuada para ver el error que se ha producido.

23) Arregla el fichero de configuración y vuelve a inciar el servicio.

</div>

[Volver](index)


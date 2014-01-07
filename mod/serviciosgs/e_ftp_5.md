---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio:  Configuración de proFTPd para usar usuarios virtuales con ldap

Al igual que otros muchos servicios proftp puede almacenar la información de autenticación de usuarios en LDAP, por lo que se suele denominar a éstos usuarios virtuales para diferenciarlos de los usuarios reales o del sistema.

En Debian lenny al instalar el paquete proftpd, se instala por dependencias el paquete proftpd-mod-ldap, por lo que no deberemos instalar ningún paquete adicional sino "activar" este método de autenticación.

Editamos el fichero /etc/proftpd/modules.conf y buscamos la línea:

        #LoadModule mod_ldap.c

La descomentamos para que cuando se reinicie el servidor cargue el módulo de LDAP.

Editamos el fichero /etc/proftpd/proftpd.conf y buscamos la línea:

        #Include /etc/proftpd/ldap.conf

También la descomentamos y editamos el fichero /etc/proftpd/ldap.conf, en el que dejamos las tres líneas siguientes:

        LDAPServer ldap://localhost/??sub LDAPDNInfo "cn=admin,dc=cursolinux,dc=net" "asdasd" LDAPDoAuth on "ou=People,dc=cursolinux,dc=net"

Donde especificamos el servidor LDAP, el nombre distinguido del usuario que se conecta, su contraseña y la ubicación de la rama que contiene los usuarios.

Además, para que puedan autenticarse usuarios con la shell (/bin/false) hay que descomentar la directiva:

        #RequireValidShell off 

Después de hacer todas estas modificaciones reiniciamos el demonio con:

        /etc/init.d/proftpd restart 

**Prueba de funcionamiento**

Vamos a crear un usuario virtual que tendrá su directorio home en /srv/ftp/usuario y como shell /bin/false para que no pueda nunca abrir una sesión en el sistema. Creamos el fichero usuario-ftp.ldif con el siguiente contenido:

        dn: cn=ftpusers,ou=Group,dc=cursolinux,dc=net objectClass: posixGroup objectClass: top cn: ftpusers gidNumber: 2002

        dn: uid=rigoberta,ou=People,dc=cursolinux,dc=net uid: rigoberta cn: Rigoberta objectclass: account objectclass: posixAccount objectclass: top uidNumber: 2002 gidNumber: 2002 homeDirectory: /srv/ftp/rigoberta userPassword: {MD5}qPXxZ/RPSWTmyZje6CcRDA== loginShell: /bin/false

Y lo añadimos al directorio con:

        ldapadd -x -D "cn=admin,dc=cursolinux,dc=net" -W -f usuario-ftp.ldif

Creamos el directorio del usuario y le damos los propietarios y permisos adecuados con:

        mkdir -p /srv/ftpusers/rigoberta 
        chgrp 2002 /srv/ftpusers 
        chown 2002 /srv/ftpusers/rigoberta 
        chmod 700 /srv/ftpusers/rigoberta

Finalmente probamos con un cliente ftp la conexión con este usuario.

[Volver](index)

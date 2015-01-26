---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Ejercicio Esquemas


La herramienta de validación desde línea de comandos que utilizaremos se llama xmllint, que pertenece al paquete debian "libxml2-utils". Para validar un fichero xml con un fichero XSD (XML Schema Definition) ejecutamos el siguiente comando:

	xmllint fichero.xml --schema fichero.xsd

####Ejemplo 1: Tipos simples

ejemplo1.xml

	<?xml version="1.0" encoding="utf-8"?>
	<nota>
  		hola
	</nota>

ejemplo1.xsd

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
		<xs:element name="nota" type="xs:string"/>
	</xs:schema>

####Ejemplo 2: Tipos complejos

[libro1.xml](fich/libro1.xml)

	<libro>
  		<autor>Miguel de Cervantes Saavedra</autor>
  		<titulo>El Quijote de la Mancha</titulo>
	</libro>

[libro1.xsd](fich/libro1.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  		<xs:element name="libro">
    		<xs:complexType>
      			<xs:sequence>
					<xs:element name="autor" type="xs:string" />
					<xs:element name="titulo" type="xs:string" />
      			</xs:sequence>
    		</xs:complexType>
  		</xs:element>
	</xs:schema>


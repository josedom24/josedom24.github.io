# Introducción al lenguaje XSD (XML Schema Definition)
---
## ¿Qué es XSD?
XSD es un formato para definir la estructura de un documento XML. XSD sustituye al anterior formato DTD, y añade funcionalidad para definir la estructura XML con más detalle.

	!xml
	<?xml version="1.0"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	 <xs:element name="note">
	   <xs:complexType>
	     <xs:sequence>
	       <xs:element name="to" type="xs:string"/>
	       <xs:element name="from" type="xs:string"/>
	       <xs:element name="heading" type="xs:string"/>
	       <xs:element name="body" type="xs:string"/>
	     </xs:sequence>
	   </xs:complexType>
	 </xs:element>
	</xs:schema>
---
## Hacer referencia al esquema

	!xml
	<?xml version="1.0"?>
	<note
	xmlns="http://www.openalfa.com"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	xsi:schemaLocation="http://www.openalfa.com note.xsd">
	  <to>Tove</to>
	  <from>Jani</from>
	  <heading>Reminder</heading>
	  <body>Don't forget me this weekend!</body>
	</note>

* Indicamos que el "namespace" al que pertenecen los elementos que aparecen en el documento es "http://www.openalfa.com".
* Indicamos que también pueden aparecer elementos del namespace "http://www.w3.org/2001/XMLSchema-instance", y deben ir precedidos por el prefijo "xsi".
* Indicamos la ubicación del esquema XSD contra el que se debe validar el documento XML ("note.xsd"). 
---
## Tipos de datos simples

	!xml
	<xs:element name="nombre_del_elemento" type="tipo_de_datos" />

* xs:string
* xs:decimal
* xs.integer
* xs:boolean
* xs:date
* xs:time

Para indicar el tipo de un atributo, por ejemplo:

	!xml
	<xs:attribute name="lang" type="xs:string" use="required"/>

---
## Restricciones (I) 

* enumeration		Defines a list of acceptable values
* fractionDigits	Specifies the maximum number of decimal places allowed. Must be equal to or greater than zero
* length		Specifies the exact number of characters or list items allowed. Must be equal to or greater than zero
* maxExclusive		Specifies the upper bounds for numeric values (the value must be less than this value)
* maxInclusive		Specifies the upper bounds for numeric values (the value must be less than or equal to this value)
* maxLength		Specifies the maximum number of characters or list items allowed. Must be equal to or greater than zero
---
## Restricciones (II) 
* minExclusive		Specifies the lower bounds for numeric values (the value must be greater than this value)
* minInclusive		Specifies the lower bounds for numeric values (the value must be greater than or equal to this value)
* minLength		Specifies the minimum number of characters or list items allowed. Must be equal to or greater than zero
* pattern		Defines the exact sequence of characters that are acceptable
* totalDigits		Specifies the exact number of digits allowed. Must be greater than zero
* whiteSpace		Specifies how white space (line feeds, tabs, spaces, and carriage returns) is handled
---
##  Ejemplo de restricciones

	!xml
	<xs:element name="age">
	  <xs:simpleType>
	    <xs:restriction base="xs:integer">
	      <xs:minInclusive value="0"/>
	      <xs:maxInclusive value="120"/>
	    </xs:restriction>
	  </xs:simpleType>
	</xs:element>
	<xs:element name="car">
	  <xs:simpleType>
	    <xs:restriction base="xs:string">
	      <xs:enumeration value="Audi"/>
	      <xs:enumeration value="Golf"/>
	      <xs:enumeration value="BMW"/>
	    </xs:restriction>
	  </xs:simpleType>
	</xs:element>
	<xs:element name="letter">
	  <xs:simpleType>
	    <xs:restriction base="xs:string">
	      <xs:pattern value="([a-z][A-Z])+"/>
	    </xs:restriction>
	  </xs:simpleType>
	</xs:element>
---
## Tipos de Datos Compuestos

	!xml
	<xs:element name="employee" type="fullpersoninfo"/>
	<xs:complexType name="personinfo">
	  <xs:sequence>
	    <xs:element name="firstname" type="xs:string"/>
	    <xs:element name="lastname" type="xs:string"/>
	  </xs:sequence>
	</xs:complexType>
	<xs:complexType name="fullpersoninfo">
	  <xs:complexContent>
	    <xs:extension base="personinfo">
	      <xs:sequence>
	        <xs:element name="address" type="xs:string"/>
	        <xs:element name="city" type="xs:string"/>
	        <xs:element name="country" type="xs:string"/>
	      </xs:sequence>
	    </xs:extension>
	  </xs:complexContent>
	</xs:complexType>
---
## Indicadores de orden

	!xml
	<xs:element name="person">
	  <xs:complexType>
	    <xs:choice>
	      <xs:element name="employee" type="employee"/>
	      <xs:element name="member" type="member"/>
	    </xs:choice>
	  </xs:complexType>
	</xs:element> 

* xs:all  – Los elementos que contiene pueden aparecer en cualquier orden.
* xs:choice – Sólo puede aparecer uno de los elementos que contiene
* xs:sequence – Los elementos que contiene deben aparecer exactamente en el mismo orden en que están definidos


---
## Indicadores de ocurrencia

	!xml
	<xs:element name="person">
	  <xs:complexType>
	    <xs:sequence>
	      <xs:element name="full_name" type="xs:string"/>
	      <xs:element name="child_name" type="xs:string" maxOccurs="10"/>
	    </xs:sequence>
	  </xs:complexType>
	</xs:element> 

* maxOccurs=”n” – Atributo que indica que el elemento puede aparecer varias veces, hasta un máximo de “n” veces. Si especificamos maxOccurs=”unbounded”, el elemento puede aparecer un número indefinido de veces.
* minOccurs=”n” – Atributo que indica que el elementos debe aparecer un mínimo de “n” veces. minOccurs=”0″, significa que el elemento es opcional, y puede no aparecer.


---
## Indicadores de grupo

* Group name – Podemos definir y asignar un nombre a un grupo de elementos de la forma:

		<xs:group name="nombre_grupo">…</xs:group>. 
	
	Una vez definido, en la definición de un tipo de datos compuesto podemos hacer referencia al mismo utilizando la sintaxis 

		<xs:group ref=”nombre_grupo”/>

* attributeGroup name – De la misma forma, podemos definir y asignar un nombre a un grupo de atributos de la forma 

		<xs:attributeGroup name=”nombre_grupo”>…</xs:attributeGroup>. 

	Una vez definido, podemos hacer referencia a dicho grupo con la sintaxis 
	
		<xs:attributegroup ref=”nombre_grupo”/>


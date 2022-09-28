Instrucciones:
==============

.. _step1:

1. Condiciones necesarias para acceder al servicio web
------------------------------------------------------

| El sitio web que se suscriba con Continental Assist para ofrecer el servicio, debe contratar un servicio de certificación https en donde sea colocada la herramienta a desarrollar.
| Continental Assist sólo se limitará a ofrecer la estructura resultante del servicio web con los datos resultantes de la compra del plan de servicio. El diseño de los frontend y la distribución será completa responsabilidad de los webmasters de los sites externos.
| Toda agencia o sitio externo que necesite utilizar los servicios en cuestión debe registrarse en el sistema como una agencia, por lo cual deben suministrar la siguiente información, adicional a la que normalmente se solicita, al personal de Continental Assist:

* Nombre del Dominio registrado correspondiente a su site (URL de la página web principal). Por ejemplo para el caso del portal **Agencia de Viajes Virtual**, sería  **“http://www.agenciadeviajesvirtual.com”**.
* Una vez registrado y activado el usuario, se le remitirá, vía correo electrónico, los datos de acceso al Sistema Continental Assist como agencia, así como el presente manual con la información de cómo implementar y utilizar los servicios y una clave de acceso **(“API KEY”)** única para que pueda utilizar el servicio.

**API KEY:** El consumo de los servicios necesita una clave encriptada, la cual es generada por el personal de sistemas de Continental Assist y representa la llave para validar el origen y el destino de las peticiones, esta llave es única e intransferible, es validada y asignada a cada agencia y cada tipo de usuario. El uso de la misma será detallado en **Cómo implementar e invocar los servicios web.**



.. _step2:

2. Flujo general
----------------

| Para un correcto uso de los servicios de Continental Assist es preciso conocer el flujo general del proceso de compra de la empresa, el cual se basa en los siguientes pasos respectivamente:

* Determinar los datos generales del viaje:
    * Definir Fecha de inicio y Fecha de fin.
    * Seleccionar Categoría.
    * Seleccionar Origen.
    * Seleccionar Destino.
    * Definir cantidad de pasajeros y la edad de los mismos.
* Seleccionar Plan:
    * Obtener información detallada de los planes (Beneficios y Precios).
    * Seleccionar plan.
* Suministrar Datos de los pasajeros.
* Seleccionar Beneficios Adicionales.
* Suminitrar datos de la tarjeta para la compra.
* Comprar.

| Luego de presionar el botón “Comprar”, se procede al proceso interno del sitio para sus respectivas validaciones y el envío de los datos correspondientes a la compra del plan de servicio.
| La respuesta que devuelva el sistema (sea positiva o negativa), tanto del servicio de compra como del resto de servicios, será enviada en formato interoperable (JSON) el cual debe ser formateado en la página receptora.



.. _step3:

3. Cómo implementar e invocar los servicios web
-----------------------------------------------

| La implementación de los servicios web corresponde a las operaciones de Cotización y Compra, los cuales son servicios ofrecidos por Continental Assist, utilizando para ello la interoperabilidad que ofrecen este tipo de tecnología. Los Servicios Web a presentar a continuación se desarrollaron utilizar el protocolo **REST**, el cual se caracteriza por no utilizar un contrato de servicio basado en **WSDL** y por utilizar el formato **JSON** en vez de **XML** para el transporte de las peticiones y respuestas.

| Para la implementación exitosa de los servicios deben llevarse a cabo las siguientes tareas:

* Incluir dentro de los **headers** de la petición el siguiente parámetro como Key: “Content-Type”, y como Value: “application/x-www-form-urlencoded”.
* Incluir dentro de los **headers** de la petición el siguiente parámetro como Key: “PHP-AUTHUSER”, y como Value la API KEY suministrada por Continental Assist.
* Los servicios web de compra, reciben como parámetros la información de los formularios, estructuradas en formato JSON, pasados como valores **POST.**

.. image:: /images/img_consulta_categorias.jpg

.. rubric:: (NOTA: La ruta “demo.continentalassist.com/restapi/v1/” es únicamente para fines de pruebas y desarrollo de los servicios).


.. centered:: Listado de Servicios

+----------------------+----------------------------------------+------------------------+
| Nombre del servicio  | Descripción y Respuesta                |  Parametros Requeridos |
+======================+========================================+========================+
| consulta_pais        | | Este webservice devuelve id y nombre | - ps                   | 
|                      | | de países al que se debe seleccionar |                        |
|                      | | el país desde donde se está haciendo |                        |
|                      | | la petición. (Este valor es requerido|                        |
|                      | | como parámetro en cada uno de los    |                        |
|                      | | servicios).                          |                        |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |    "resultado": [                      |                        |
|                      |    {                                   |                        |
|                      |      "id": "47",                       |                        |
|                      |      "pais": "Americas"                |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "20",                       |                        |
|                      |      "pais": "Antigua and Barbuda"     |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "1",                        |                        |
|                      |      "pais": "Argentina"               |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "36",                       |                        |
|                      |      "pais": "Aruba"                   |                        |
|                      |    }                                   |                        |
|                      |    ],                                  |                        |
|                      |    "cantidad": 4,                      |                        |
|                      |    "error": false                      |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_categorias| | Devuelve el id y el nombre de las    | - ps                   | 
| | _x_pais_dias       | | categorías correspondientes a los    | - id_lenguaje          |
|                      | | el país desde donde se está haciendo | - id_pais              |
|                      | | a las características de la agencia  | - fecha_desde          |
|                      | | solicitante.                         | - fecha_hasta          |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "id_categoria": "24",              |                        |
|                      |     "categoria": "Planes por Viaje"    |                        |
|                      |   },                                   |                        |
|                      |   {                                    |                        |
|                      |     "id_categoria": "23",              |                        |
|                      |     "categoria": "Anuales-Multiviajes" |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 2,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_origenes  | | Devuelve id y nombre de paises que   | - ps                   | 
|                      | | determinan los origenes permitidos   |                        |
|                      | | para Continental Assist.             |                        |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "iso_country": "AL",               |                        |
|                      |     "categoria": "Planes por Viaje"    |                        |
|                      |   },                                   |                        |
|                      |   {                                    |                        |
|                      |     "id_categoria": "23",              |                        |
|                      |     "categoria": "Anuales-Multiviajes" |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 2,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| body row 2           |                                        |                        |
+----------------------+----------------------------------------+------------------------+


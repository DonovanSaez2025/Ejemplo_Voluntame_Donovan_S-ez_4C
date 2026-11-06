# VoluntaMe: Plataforma de Gestión de Voluntariado

## Descripción
VoluntaMe es una okatafirna wev creada para hacer conexiones de personas con iniciativas comunitarias y solidarias. Donde el objetivo principal es permitir que cualquier usuario pueda liderar una misión de ayuda o unirse de voluntario a las ya existentes.

Este proyecto fue desarrollado enteramente por mí, como parte de mi certificación Fullstack de Skillnest, poniendo énfasis en las buenas prácticas de programación, seguridad de datos y arquitectura escalable.

---

## Tecnologías y arquitectura
El sistema está construido bajo el patrón de diseño MVC (Modelo-Vista-Controlador), lo que garantiza un código ordenado y mantenible.

* **Backend:** Python con Flask (Blueprints).
* **Base de Datos:** MySQL con relaciones.
* **Seguridad:** Encriptación de contraseñas con Bcrypt y manejo seguro de sesiones.
* **Frontend:** Plantillas Jinja2 con diseño responsivo mediante Bootstrap.

---

## Funcionalidades clave

### 1. Seguridad y usuarios
Más allá de un registro simple, el sistema cuenta con validaciones estrictas para asegurar que los correos sean únicos y las contraseñas seguras. Protegemos las rutas para que solo usuarios autenticados puedan acceder a la plataforma.

### 2. Gestión inteligente de misiones
Los usuarios pueden crear, ver y administrar misiones de voluntariado.
* **Protección de propiedad:** Implementé una lógica de backend que asegura que solo el creador de una misión pueda editarla o eliminarla, previniendo accesos no autorizados mediante manipulación de URLs.
* **Validaciones de negocio:** El sistema impide crear eventos en fechas pasadas y controla que los cupos de voluntarios sean lógicos (entre 2 y 20 personas).

### 3. La funcionalidad "Volunta-Me"
Es el corazón de la aplicación. Permite que los usuarios se inscriban en misiones con un solo clic.
* El sistema detecta automáticamente si el usuario ya participa en la misión.
* Si ya está inscrito, el botón de registro desaparece y confirma su asistencia.
* Se despliega en tiempo real la lista de todos los voluntarios unidos a la causa.

---

## Autor
**Donovan Sáez** - Desarrollador Fullstack Python

Contacto: *donovansaez@liceovvh.cl*
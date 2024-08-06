# djusers

`djusers` es una aplicación web simple desarrollada en Django para la gestión de usuarios.

## Instalación

### Crear un Entorno Virtual

Para mantener las dependencias del proyecto aisladas, es recomendable usar un entorno virtual. Sigue estos pasos para crear y activar un entorno virtual:

1. **Instalar `venv`** (si no lo tienes ya instalado):

   ```bash
   sudo apt install python3-venv
   ```

2. **Crear un Entorno Virtual**:

   ```bash
   python3 -m venv /ruta/al/entorno-virtual
   ```

3. **Activar el Entorno Virtual**:

   ```bash
   source /ruta/al/entorno-virtual/bin/activate
   ```

### Clonar el Repositorio

Descarga el código fuente del proyecto desde GitHub:

```bash
git clone https://github.com/luirro777/djusers/
cd djusers/
```

### Instalar Dependencias

Dentro del entorno virtual, instala Django:

```bash
pip install django==4.2
```

### Configurar y Ejecutar la Aplicación

Realiza las migraciones de la base de datos y arranca el servidor de desarrollo:

1. **Crear las Migraciones**:

   ```bash
   python manage.py makemigrations
   ```

2. **Aplicar las Migraciones**:

   ```bash
   python manage.py migrate
   ```

3. **Iniciar el Servidor de Desarrollo**:

   ```bash
   python manage.py runserver
   ```

## Acceder a la Aplicación

Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes rutas:

- **Registro**: [http://127.0.0.1:8000/users/register/](http://127.0.0.1:8000/users/register/)
- **Login**: [http://127.0.0.1:8000/users/login/](http://127.0.0.1:8000/users/login/)
- **Perfil**: [http://127.0.0.1:8000/users/profile/](http://127.0.0.1:8000/users/profile/)

## TODO

- Instrucciones para desplegar en entornos de producción.

## Contacto

Para cualquier consulta o soporte, puedes contactarme en [luisromano@gmail.com](mailto:luisromano@gmail.com).


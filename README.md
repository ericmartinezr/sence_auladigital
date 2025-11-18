# Autonavegador para Aula Sence

Actualmente para mantener actualizada las horas dedicadas al curso
se debe realizar una navegación manual en el aula.

Esto es extremadamente engorroso y distrae del curso mismo, por lo que escribí esto
tratando de ahorrarme ese problema.

Por defecto:

- Se ejecuta cada 15 minutos (configurable en consts.py)
- Realiza máximo un total de 12 iteraciones (configurable en consts.py)

Se que hay extensiones y otras aplicaciones que hacen esto, pero estaba aburrido :D.
Además no hace un simple refresh, navega de una parte del sitio a otra, para asegurar la interacción con el sitio.

Ejecución:

- Nota: Se asume un ambiente Unix. Esto se desarrolló y probó (a medias) en un WSL bajo Windows 10

**Generación de ambiente virtual**

```sh
python -m venv .venv
```

**Activación de ambiente virtual**

```sh
source .venv/bin/activate
```

**Instalación de dependencias**

```sh
pip install -r requirements.txt
```

**Ejecución**

```sh
python main.py
```

El log queda en app.log

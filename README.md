# Caso_Covid19

Proyecto en Python para consultar datos publicos de COVID-19 por departamento desde datos.gov.co.

## Que hace

- Solicita un departamento y un limite de registros.
- Consulta el dataset publico `gt2j-8ykr` mediante `sodapy`.
- Muestra los resultados en consola.

## Estructura

- `main.py`: punto de entrada de la aplicacion.
- `api/api.py`: logica de consulta a la API de Socrata.
- `ui/ui.py`: lectura y validacion de entrada, y presentacion de resultados.
- `run_api.py`: script de prueba manual de la API.

## Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta la aplicacion principal:

```bash
python main.py
```

Tambien puedes usar argumentos:

```bash
python main.py --departamento Bogota --limite 5
```

Si no usas argumentos, el programa solicita los datos por consola.

Luego ingresa:

- El nombre del departamento.
- La cantidad de registros a consultar.

## Variables opcionales

Puedes cambiar la fuente de datos con estas variables de entorno:

- `COVID_BASE_URL`: por defecto `www.datos.gov.co`
- `COVID_DATASET_ID`: por defecto `gt2j-8ykr`

## Prueba rapida

Para validar la conexion basica a la API:

```bash
python run_api.py
```

## Notas

- La entrada se valida antes de hacer la consulta.
- Si no hay datos o ocurre un error de consulta, la aplicacion devuelve una salida vacia y registra el error en el logger.
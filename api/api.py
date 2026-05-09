import os
import logging
from typing import List, Any

from sodapy import Socrata

logger = logging.getLogger(__name__)


def fetch_covid_data(nombre_departamento: str, limite_registros: int) -> List[Any]:
    """Consulta el dataset publico y devuelve una lista de registros."""
    BASE_URL = os.getenv("COVID_BASE_URL", "www.datos.gov.co")
    DATASET_ID = os.getenv("COVID_DATASET_ID", "gt2j-8ykr")

    if not isinstance(nombre_departamento, str) or not nombre_departamento.strip():
        logger.error("nombre_departamento invalido: %r", nombre_departamento)
        return []
    if not isinstance(limite_registros, int) or limite_registros <= 0:
        logger.error("limite_registros invalido: %r", limite_registros)
        return []

    try:
        cliente = Socrata(BASE_URL, None, timeout=10)

        query = f"departamento_nom='{nombre_departamento.strip().upper()}'"
        logger.debug(
            "Realizando consulta Socrata: dataset=%s where=%s limit=%s",
            DATASET_ID,
            query,
            limite_registros,
        )

        resultados = cliente.get(DATASET_ID, where=query, limit=limite_registros)

        if not resultados:
            logger.info("No se encontraron datos para el departamento: %s", nombre_departamento)
            return []

        return resultados

    except Exception:
        logger.exception("Error al obtener los datos desde Socrata (dataset=%s)", DATASET_ID)
        return []

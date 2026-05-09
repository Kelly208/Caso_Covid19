import argparse

from api.api import fetch_covid_data
from ui.ui import display_results, get_user_input


def parse_args():
    parser = argparse.ArgumentParser(
        description="Consulta datos COVID-19 por departamento"
    )
    parser.add_argument(
        "-d",
        "--departamento",
        help="Nombre del departamento a consultar",
    )
    parser.add_argument(
        "-l",
        "--limite",
        type=int,
        help="Numero maximo de registros a consultar",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.departamento and args.limite:
        nombre_departamento = args.departamento.strip()
        limite_registros = args.limite
    else:
        nombre_departamento, limite_registros = get_user_input()

    nombre_departamento = nombre_departamento.strip().upper()

    resultados = fetch_covid_data(nombre_departamento, limite_registros)

    if resultados:
        display_results(resultados)
    else:
        print("No se encontraron datos.")


if __name__ == "__main__":
    main()

from sodapy import Socrata


def main():
    """Ejecuta una consulta manual de ejemplo contra la API publica."""
    client = Socrata("www.datos.gov.co", None)
    data = client.get("gt2j-8ykr", limit=5)
    print(data)


if __name__ == "__main__":
    main()

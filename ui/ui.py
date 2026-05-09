def get_user_input():
    """Solicita y valida el departamento y el limite de registros."""
    while True:
        nombre_departamento = input("Ingrese el nombre del departamento: ").strip()
        if not nombre_departamento:
            print("El nombre del departamento no puede estar vacio. Intente de nuevo.")
            continue

        limite_raw = input("Ingrese el numero de registros a consultar (1-1000): ").strip()
        try:
            limite_registros = int(limite_raw)
            if limite_registros <= 0:
                print("El numero de registros debe ser mayor que 0.")
                continue
            if limite_registros > 1000:
                print("Maximo permitido 1000. Se usara 1000.")
                limite_registros = 1000
        except ValueError:
            print("Ingrese un numero entero valido para el limite.")
            continue

        return nombre_departamento, limite_registros


def display_results(results):
    """Muestra resultados en consola."""
    print("\nResultados de la consulta:")
    try:
        print(results.to_string(index=False))
    except Exception:
        import json

        print(json.dumps(results, indent=4, ensure_ascii=False))
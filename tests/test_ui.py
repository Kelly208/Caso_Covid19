from unittest.mock import patch

from ui.ui import get_user_input


@patch("builtins.input", side_effect=["Bogota", "5"])
def test_get_user_input_valid(mock_input):
    nombre_departamento, limite_registros = get_user_input()

    assert nombre_departamento == "Bogota"
    assert limite_registros == 5


@patch("builtins.input", side_effect=["", "Bogota", "abc", "Bogota", "5"])
@patch("builtins.print")
def test_get_user_input_retries_until_valid(mock_print, mock_input):
    nombre_departamento, limite_registros = get_user_input()

    assert nombre_departamento == "Bogota"
    assert limite_registros == 5
    mock_print.assert_any_call("El nombre del departamento no puede estar vacio. Intente de nuevo.")
    mock_print.assert_any_call("Ingrese un numero entero valido para el limite.")

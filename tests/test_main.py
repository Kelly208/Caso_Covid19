from unittest.mock import MagicMock, patch

import main


@patch("main.fetch_covid_data")
@patch("main.display_results")
@patch("main.parse_args")
def test_main_uses_cli_arguments(mock_parse_args, mock_display_results, mock_fetch):
    mock_parse_args.return_value = MagicMock(departamento="Bogota", limite=3)
    mock_fetch.return_value = [{"departamento_nom": "BOGOTA", "casos": 1}]

    main.main()

    mock_fetch.assert_called_once_with("BOGOTA", 3)
    mock_display_results.assert_called_once_with(
        [{"departamento_nom": "BOGOTA", "casos": 1}]
    )


@patch("main.get_user_input")
@patch("main.fetch_covid_data")
@patch("main.display_results")
@patch("main.parse_args")
def test_main_falls_back_to_interactive_input(
    mock_parse_args, mock_display_results, mock_fetch, mock_get_user_input
):
    mock_parse_args.return_value = MagicMock(departamento=None, limite=None)
    mock_get_user_input.return_value = ("Bogota", 2)
    mock_fetch.return_value = [{"departamento_nom": "BOGOTA", "casos": 2}]

    main.main()

    mock_get_user_input.assert_called_once()
    mock_fetch.assert_called_once_with("BOGOTA", 2)
    mock_display_results.assert_called_once_with(
        [{"departamento_nom": "BOGOTA", "casos": 2}]
    )

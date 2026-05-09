from unittest.mock import MagicMock, patch

from api.api import fetch_covid_data


@patch("api.api.Socrata")
def test_fetch_covid_data_returns_results(mock_socrata):
    fake_client = MagicMock()
    fake_client.get.return_value = [{"departamento_nom": "BOGOTA", "casos": 10}]
    mock_socrata.return_value = fake_client

    results = fetch_covid_data("bogota", 5)

    assert results == [{"departamento_nom": "BOGOTA", "casos": 10}]
    mock_socrata.assert_called_once_with("www.datos.gov.co", None, timeout=10)
    fake_client.get.assert_called_once_with(
        "gt2j-8ykr",
        where="departamento_nom='BOGOTA'",
        limit=5,
    )


@patch("api.api.Socrata")
def test_fetch_covid_data_returns_empty_list_when_no_results(mock_socrata):
    fake_client = MagicMock()
    fake_client.get.return_value = []
    mock_socrata.return_value = fake_client

    results = fetch_covid_data("bogota", 5)

    assert results == []


@patch("api.api.Socrata")
def test_fetch_covid_data_returns_empty_list_on_exception(mock_socrata):
    mock_socrata.side_effect = RuntimeError("network error")

    results = fetch_covid_data("bogota", 5)

    assert results == []

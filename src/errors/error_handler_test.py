from src.views.http_types.http_response import HttpResponse

from .error_handler import handle_errors
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_generic_handle_errors():
    response: HttpResponse = handle_errors(Exception)

    assert response.status_code == 500
    assert "errors" in response.body

    assert len(response.body["errors"]) == 1
    assert "title" in response.body["errors"][0]
    assert "detail" in response.body["errors"][0]

    assert response.body["errors"][0]["title"] == "Server Error"

def test_custom_handle_errors():
    response: HttpResponse = handle_errors(HttpUnprocessableEntityError("test_error"))

    assert response.status_code == 422
    assert "errors" in response.body

    assert len(response.body["errors"]) == 1
    assert "title" in response.body["errors"][0]
    assert "detail" in response.body["errors"][0]

    assert response.body["errors"][0]["title"] == "UnprocessableEntity"
    assert response.body["errors"][0]["detail"] == "test_error"

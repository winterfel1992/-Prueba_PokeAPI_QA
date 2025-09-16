from behave import given, then
from requests import Response

@given(r'la base URL "{base_url}"$')
def step_set_base_url(context, base_url):
    context.client.base_url = base_url

@then(r'la respuesta tiene status {code:d}$')
def step_status_code(context, code):
    assert isinstance(context.last_response, Response)
    assert context.last_response.status_code == code, (
        f"Esperado {code}, obtenido {context.last_response.status_code}"
    )

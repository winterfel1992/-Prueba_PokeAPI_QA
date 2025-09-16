from behave import when, then
from src.utils.timing import assert_duration_lt
from src.utils.validators import (
    assert_json_has_required_fields,
    assert_content_type_json,
    assert_security_headers,
    validate_pokemon_schema,
    is_2xx,
)

@when(r'consulto el pokemon "{name}"$')
def step_get_pokemon_name(context, name):
    r = context.client.get_pokemon(name.strip('"'))
    context.last_response = r
    context.logger.info(f"GET pokemon/{name} -> {r.status_code}")

@when(r'consulto el pokemon por id "{pid}"$')
def step_get_pokemon_id(context, pid):
    r = context.client.get_pokemon(pid)
    context.last_response = r

@then(r'el tiempo de respuesta es menor a 2 segundos$')
def step_duration(context):
    assert_duration_lt(context.last_response, 2.0)

@then(r'el header "Content-Type" contiene "application/json"$')
def step_ct(context):
    assert_content_type_json(context.last_response)

@then(r'el JSON contiene los campos obligatorios$')
def step_required_fields(context):
    data = context.last_response.json()
    assert_json_has_required_fields(data, ["id", "name", "abilities", "moves", "stats"])

@then(r'el schema del JSON es válido$')
def step_schema(context):
    if is_2xx(context.last_response.status_code):
        validate_pokemon_schema(context.last_response.json())

@then(r'la respuesta cumple condiciones de límite$')
def step_boundary(context):
    code = context.last_response.status_code
    assert code in (200, 404), f"Boundary inválido: {code}"

@then(r'obtengo un status code apropiado$')
def step_edge_status(context):
    assert context.last_response.status_code in (200, 400, 404, 422)
    if context.last_response.status_code == 200:
        validate_pokemon_schema(context.last_response.json())

@then(r'los headers incluyen seguridad y cache apropiados$')
def step_headers(context):
    assert_content_type_json(context.last_response)
    assert_security_headers(context.last_response)

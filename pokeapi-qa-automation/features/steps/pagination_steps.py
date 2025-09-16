from behave import when, then
from src.utils.validators import (
    assert_content_type_json,
    assert_page_size_between,
    assert_default_limit_is_20,
    extract_names_from_results,
    assert_links_coherent,
)
from src.api.models import Pokemon

@when(r'consulto la lista con limit {limit} y offset {offset}$')
def step_list(context, limit, offset):
    r = context.client.get_pokemon_list(limit=limit, offset=offset)
    context.last_response = r

@then(r'la página retorna 20 resultados por defecto$')
def step_default_limit(context):
    assert_default_limit_is_20(context.last_response)

@then(r'los enlaces next y previous son coherentes$')
def step_links(context):
    assert_links_coherent(context.last_response.json())

@then(r'la página retorna 1 resultado$')
def step_one(context):
    assert_page_size_between(context.last_response.json(), 1, 1)

@then(r'la página retorna entre 1 y 1000 resultados$')
def step_range(context):
    assert_page_size_between(context.last_response.json(), 1, 1000)

@then(r'la página retorna 0 resultados$')
def step_zero(context):
    assert_page_size_between(context.last_response.json(), 0, 0)

@when('consulto dos veces la lista con limit 20 y offset 0')
def step_consistency(context):
    r1 = context.client.get_pokemon_list(limit=20, offset=0)
    r2 = context.client.get_pokemon_list(limit=20, offset=0)
    context.consistency_pair = (r1.json(), r2.json())
    context.last_response = r2

@then(r'los resultados son consistentes en un intervalo corto$')
def step_consistency_check(context):
    a, b = context.consistency_pair
    names_a = extract_names_from_results(a)
    names_b = extract_names_from_results(b)
    assert names_a == names_b, "Resultados no consistentes"

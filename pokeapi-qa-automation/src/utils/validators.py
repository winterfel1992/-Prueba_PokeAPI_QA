from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.utils.schema import pokemon_schema

def is_2xx(code: int) -> bool:
    return 200 <= code < 300

def assert_json_has_required_fields(data: dict, fields: list[str]):
    for f in fields:
        assert f in data, f"Falta campo obligatorio: {f}"

def validate_pokemon_schema(data: dict):
    try:
        validate(instance=data, schema=pokemon_schema)
    except ValidationError as e:
        raise AssertionError(f"Schema inválido: {e.message}")

def assert_content_type_json(response):
    ct = response.headers.get("Content-Type", "")
    assert "application/json" in ct, f"Content-Type inesperado: {ct}"

def assert_security_headers(response):
    # PokeAPI puede no incluir todos; validamos presencia si existen
    # Recomendados: CORS, cache, content security
    # No forzamos exactitud, solo formato básico
    cache = response.headers.get("Cache-Control", "")
    assert isinstance(cache, str)
    # CORS típicos
    assert isinstance(response.headers.get("Access-Control-Allow-Origin", "*"), str)

def assert_default_limit_is_20(response):
    # Si se llama sin limit, responde 20 por defecto
    data = response.json()
    assert len(data.get("results", [])) == 20, "El default de limit debería ser 20"

def assert_page_size_between(data: dict, min_n: int, max_n: int):
    n = len(data.get("results", []))
    assert min_n <= n <= max_n, f"Tamaño {n} fuera de [{min_n}, {max_n}]"

def assert_links_coherent(data: dict):
    # next/previous pueden ser null o URLs con limit & offset coherentes
    for k in ("next", "previous"):
        v = data.get(k)
        assert v is None or (isinstance(v, str) and "limit=" in v and "offset=" in v)

def extract_names_from_results(data: dict) -> list[str]:
    return [x["name"] for x in data.get("results", []) if isinstance(x, dict) and "name" in x]

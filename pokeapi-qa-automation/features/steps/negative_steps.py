from behave import when, then
from requests import exceptions

@when(r'consulto la lista con limit "{limit}" y offset "{offset}"$')
def step_list_str(context, limit, offset):
    r = context.client.get_pokemon_list(limit=limit, offset=offset)
    context.last_response = r

@then(r'la respuesta tiene status 400 o 422$')
def step_4xx(context):
    assert context.last_response.status_code in (400, 422)

@when(r'realizo 100 requests rápidos al endpoint de lista$')
def step_burst(context):
    codes = []
    for _ in range(100):
        r = context.client.get_pokemon_list(limit=20, offset=0)
        codes.append(r.status_code)
    context.rate_codes = codes

@then(r'eventualmente recibo 429 o la API responde con degradación controlada$')
def step_rate_outcome(context):
    assert 429 in context.rate_codes or all(c == 200 for c in context.rate_codes)

@when(r'consulto el pokemon "ditto" con timeout 0.001$')
def step_timeout(context):
    try:
        context.client.set_timeout(0.001)
        r = context.client.get_pokemon("ditto")
        context.last_response = r
        context.timeout_hit = False
    except exceptions.Timeout:
        context.timeout_hit = True
    finally:
        context.client.set_timeout(10)

@then(r'la request expira por timeout$')
def step_timeout_assert(context):
    assert getattr(context, "timeout_hit", False) is True

@then(r'la API no ejecuta payloads ni filtra datos sensibles$')
def step_injection_safe(context):
    text = context.last_response.text.lower()
    forbidden = ["stack trace", "internal server error", "password", "etc/passwd"]
    assert not any(t in text for t in forbidden)

@then(r'la respuesta tiene un status seguro \(4xx\)$')
def step_4xx_safe(context):
    assert 400 <= context.last_response.status_code < 500

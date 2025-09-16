def assert_duration_lt(response, seconds: float):
    # requests almacena elapsed
    duration = response.elapsed.total_seconds()
    assert duration < seconds, f"Respuesta tardó {duration:.3f}s, límite {seconds}s"

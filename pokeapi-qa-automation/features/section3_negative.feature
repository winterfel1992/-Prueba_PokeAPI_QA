Feature: Pruebas negativas avanzadas
  Validar manejo de errores y robustez.

  Background:
    Given la base URL "https://pokeapi.co/api/v2"

  @404
  Scenario: 404 Not Found en pokemon inexistente
    When consulto el pokemon por id "9999999"
    Then la respuesta tiene status 404

  @400
  Scenario: 400 Bad Request por parámetros malformados
    When consulto la lista con limit "abc" y offset "xyz"
    Then la respuesta tiene status 400 o 422

  @429
  Scenario: 429 Too Many Requests por rate limiting
    When realizo 100 requests rápidos al endpoint de lista
    Then eventualmente recibo 429 o la API responde con degradación controlada

  @timeout
  Scenario: Timeout testing simulando conexión lenta
    When consulto el pokemon "ditto" con timeout 0.001
    Then la request expira por timeout

  @injection
  Scenario Outline: Inyección de parámetros
    When consulto el pokemon "<payload>"
    Then la API no ejecuta payloads ni filtra datos sensibles
    And la respuesta tiene un status seguro (4xx)
    Examples:
      | payload         |
      | "' OR '1'='1"   |
      | "1; DROP TABLE" |
      | "../../etc/passwd" |

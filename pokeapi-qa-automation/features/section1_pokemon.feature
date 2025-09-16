Feature: Endpoint de detalle de Pokémon
  Como QA, quiero validar el endpoint GET /pokemon/{pokemon} aplicando técnicas de testing.

  Background:
    Given la base URL "https://pokeapi.co/api/v2"

  @happy_path
  Scenario: Happy path con nombre válido
    When consulto el pokemon "pikachu"
    Then la respuesta tiene status 200
    And el tiempo de respuesta es menor a 2 segundos
    And el header "Content-Type" contiene "application/json"
    And el JSON contiene los campos obligatorios
    And el schema del JSON es válido

  @boundary
  Scenario Outline: Boundary testing con IDs límite
    When consulto el pokemon por id "<id>"
    Then la respuesta cumple condiciones de límite
    Examples:
      | id   |
      | 1    |
      | 1010 |
      | 1011 |

  @edge_cases
  Scenario Outline: Nombres con caracteres especiales
    When consulto el pokemon "<name>"
    Then obtengo un status code apropiado
    Examples:
      | name          |
      | "   "         |
      | "pi%kachu"    |
      | "नमस्ते"      |
      | "pikachu\n"   |

  @headers
  Scenario: Validación de headers de respuesta
    When consulto el pokemon "bulbasaur"
    Then los headers incluyen seguridad y cache apropiados

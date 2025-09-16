Feature: Paginación de listado de Pokémon
  Para garantizar integridad de datos y navegación.

  Background:
    Given la base URL "https://pokeapi.co/api/v2"

  @pagination_normal
  Scenario Outline: Paginación normal
    When consulto la lista con limit 20 y offset <offset>
    Then la respuesta tiene status 200
    And la página retorna 20 resultados por defecto
    And los enlaces next y previous son coherentes
    Examples:
      | offset |
      | 0      |
      | 20     |
      | 40     |

  @limits
  Scenario: Límites extremos
    When consulto la lista con limit 1 y offset 0
    Then la respuesta tiene status 200
    And la página retorna 1 resultado

    When consulto la lista con limit 1000 y offset 0
    Then la respuesta tiene status 200
    And la página retorna entre 1 y 1000 resultados

  @offset_out_of_range
  Scenario: Offset fuera de rango
    When consulto la lista con limit 20 y offset 999999
    Then la respuesta tiene status 200
    And la página retorna 0 resultados

  @negative_params
  Scenario: Parámetros negativos
    When consulto la lista con limit -1 y offset -20
    Then obtengo un status code apropiado para parámetros inválidos

  @consistency
  Scenario: Consistencia temporal
    When consulto dos veces la lista con limit 20 y offset 0
    Then los resultados son consistentes en un intervalo corto

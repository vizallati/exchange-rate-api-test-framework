Feature: Access Exchange Rate Data via Standard API Endpoint
  As a user of the ExchangeRate-API, I want to access exchange rate data using the Standard API endpoint
  by getting conversion rates from my chosen base currency to all supported currencies

  Scenario Outline: Basic Exchange Rate Retrieval
    When I send a request to the standard requests endpoint, specifying a "<base_currency>"
    Then API returns a JSON object with exchange rates from the specified "<base_currency>" to all supported currency codes
    Examples:
      |base_currency  |
      | USD           |

  Scenario Outline: Error Handling - Invalid Base Currency
    When I send a request to the standard requests endpoint, specifying a "<base_currency>"
    Then API returns a JSON object with "<expected_error_type>" error type
    Examples:
      |base_currency  |expected_error_type|
      | UST           |unsupported-code   |

  Scenario Outline: Basic Exchange Rate Retrieval with invalid api key
    When I send a request to the standard requests endpoint, specifying a "<base_currency>" with "<invalid_api_key>"
    Then API returns a JSON object with "<expected_error_type>" error type
    Examples:
      |base_currency  |invalid_api_key     |expected_error_type|
      | USD           |  6jjA690e41fad6d6  | invalid-key       |
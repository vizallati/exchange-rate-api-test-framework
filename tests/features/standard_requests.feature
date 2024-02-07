Feature: Access Exchange Rate Data via Standard API Endpoint
  As a user of the ExchangeRate-API, I want to access exchange rate data using the Standard API endpoint
  by getting conversion rates from my chosen base currency to all supported currencies

  Scenario Outline: Basic Exchange Rate Retrieval
    When I send a request to the API specifying a "<base_currency>"
    Then API returns a JSON object with exchange rates from the specified "<base_currency>" to all supported currency codes
    Examples:
      |base_currency  |
      | USD           |

  Scenario Outline: Error Handling - Invalid Base Currency
    When I send a request to the API specifying a "<base_currency>"
    Then API returns a JSON object with "<expected_error_type>"
    Examples:
      |base_currency  |expected_error_type|
      | UST           |unsupported-code   |
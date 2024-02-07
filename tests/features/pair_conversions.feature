Feature: Pair Conversion API Endpoint
  As a user of the Pair Conversion API endpoint, I want to be able to convert between two specific currencies

  Scenario Outline: Convert between two specific currencies
    When I send a request to pair conversions endpoint with "<base_code>", "<target_code>", "<amount>"
    Then API returns a JSON object containing the conversion rate and "<conversion_result>" with correct "<base_code>" and "<target_code>"
    Examples:
      |base_code |target_code| amount|conversion_result|
      | USD      | GBP       |100    | True            |
      | USD      | GBP       |None   | False           |

  Scenario Outline: Convert between two specific currencies invalid codes
    When I send a request to pair conversions endpoint with "<base_code>", "<target_code>", "<amount>"
    Then API returns a JSON object with "unsupported-code" error type
    Examples:
      |base_code |target_code| amount|
      | UST      | GBP       |100    |
      | USD      | GPB       |100    |
      | UST      | GPB       |100    |
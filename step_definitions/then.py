from pytest_bdd import parsers
from pytest_bdd.steps import then
from core.constants import all_supported_currencies
from core.utils import Context
from assertpy import assert_that


@then(parsers.cfparse('API returns a JSON object with exchange rates from the specified "{base_currency}" to all '
                      'supported currency codes'))
def check_exchange_rates(base_currency):
    json_response = Context.response.json()
    assert_that(Context.response.status_code).is_equal_to(200)
    assert_that(json_response['result']).is_equal_to('success')
    assert_that(json_response['base_code']).is_equal_to(base_currency)
    assert_that(json_response['conversion_rates']).is_length(all_supported_currencies)


@then(parsers.cfparse('API returns a JSON object with "{expected_error_type}"'))
def check_exchange_rates(expected_error_type):
    json_response = Context.response.json()
    assert_that(Context.response.status_code).is_equal_to(404)
    assert_that(json_response['error-type']).is_equal_to(expected_error_type)

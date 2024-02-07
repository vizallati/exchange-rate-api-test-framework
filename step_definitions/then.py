from pytest_bdd import parsers
from pytest_bdd.steps import then
from core.constants import all_supported_currencies, HTTPStatus
from core.utils import Context
from assertpy import assert_that


@then(parsers.cfparse('API returns a JSON object with exchange rates from the specified "{base_currency}" to all '
                      'supported currency codes'))
def check_exchange_rates(base_currency):
    json_response = Context.response.json()
    assert_that(Context.response.status_code).is_equal_to(HTTPStatus.OK.value)
    assert_that(json_response['result']).is_equal_to('success')
    assert_that(json_response['base_code']).is_equal_to(base_currency)
    assert_that(json_response['conversion_rates']).is_length(all_supported_currencies)


@then(parsers.cfparse('API returns a JSON object with "{expected_error_type}"'))
def check_standard_requests_error(expected_error_type):
    json_response = Context.response.json()
    expected_status_code = HTTPStatus.FORBIDDEN.value if expected_error_type == 'invalid-key' else HTTPStatus.NOT_FOUND.value
    assert_that(Context.response.status_code).is_equal_to(expected_status_code)
    assert_that(json_response['result']).is_equal_to('error')
    assert_that(json_response['error-type']).is_equal_to(expected_error_type)


@then(parsers.cfparse(
    'API returns a JSON object containing the conversion rate and "{conversion_result}" with correct "{base_code}" '
    'and "{target_code}"'))
def check_conversion_rate_response(conversion_result, base_code, target_code):
    conversion_result = eval(conversion_result)
    json_response = Context.response.json()
    assert_that(Context.response.status_code).is_equal_to(HTTPStatus.OK.value)
    assert_that(json_response['result']).is_equal_to('success')
    assert_that(json_response['conversion_rate']).is_true()
    if conversion_result:
        assert_that(json_response['conversion_result']).is_true()
    assert_that(json_response['base_code']).is_equal_to(base_code)
    assert_that(json_response['target_code']).is_equal_to(target_code)

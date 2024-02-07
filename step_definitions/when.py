from pytest_bdd import parsers
from pytest_bdd.steps import when
from dsl.exchange_rate import ExchangeRate
from core.utils import Context


@when(parsers.cfparse('I send a request to the standard requests endpoint, specifying a "{base_currency}"'))
def get_exchange_rates(base_currency):
    Context.response = ExchangeRate().standard_requests(currency=base_currency)


@when(parsers.cfparse('I send a request to the standard requests endpoint, specifying a "{base_currency}" with "{'
                      'invalid_api_key}"'))
def get_exchange_rates_invalid_creds(base_currency, invalid_api_key):
    Context.response = ExchangeRate().standard_requests(currency=base_currency, api_key=invalid_api_key)


@when(parsers.cfparse('I send a request to pair conversions endpoint with "{base_code}", "{target_code}", '
                      '"{amount}"'))
def get_pair_conversion(base_code, target_code, amount):
    amount = None if amount == 'None' else amount
    Context.response = ExchangeRate().pair_conversions(input_currency=base_code, output_currency=target_code,
                                                       amount=amount)

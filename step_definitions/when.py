from pytest_bdd import parsers
from pytest_bdd.steps import when
from dsl.exchange_rate import ExchangeRate
from core.utils import Context


@when(parsers.cfparse('I send a request to the API specifying a "{base_currency}"'))
def get_exchange_rates(base_currency):
    Context.response = ExchangeRate().standard_requests(currency=base_currency)

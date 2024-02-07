import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('EX-001')
@scenario('features/standard_requests.feature', 'Basic Exchange Rate Retrieval')
def test_exchange_rate_retrieval():
    pass


@pytest.mark.case_id('EX-002')
@scenario('features/standard_requests.feature', 'Error Handling - Invalid Base Currency')
def test_invalid_base_currency():
    pass

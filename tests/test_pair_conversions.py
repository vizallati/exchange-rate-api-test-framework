import pytest
from pytest_bdd import scenario
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('EX-004')
@scenario('features/pair_conversions.feature', 'Convert between two specific currencies')
def test_exchange_rate_conversion():
    pass


@pytest.mark.case_id('EX-005', 'EX-006', 'EX-007')
@scenario('features/pair_conversions.feature', 'Convert between two specific currencies invalid codes')
def test_exchange_rate_conversion_invalid_codes():
    pass

import pytest
from core.utils import load_yaml, Context, add_tags_allure, add_links_allure
from allure_commons import plugin_manager
from allure_pytest_bdd.pytest_bdd_listener import PytestBDDListener


@pytest.fixture(scope='session', autouse=True)
def load_config():
    """Fixture for loading config files used by tests to memory."""
    load_yaml('settings.yml')


@pytest.fixture(autouse=True)
def delete_response_attribute():
    """Fixture to delete the 'response' attribute from the 'Context' class after each test."""
    yield
    if hasattr(Context, 'response'):
        delattr(Context, 'response')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    pytest hook function to customize the Allure report for BDD scenarios.

    This hook is triggered after the test item has been executed, and it customizes the Allure report by:
    1. Retrieving the test result and setting it in the global `settings.test_result`.
    2. Adding tags to the Allure report based on pytest markers.
    3. Adding links to the Allure report based on test case IDs.
    4. Setting the description of the test result in the Allure report.

    Parameters:
    - item: The pytest item object.

    Returns:
    None
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        for plugin in plugin_manager.list_name_plugin():
            p = plugin[1]
            if isinstance(p, PytestBDDListener):
                Context.test_result = p.lifecycle._get_item()
                add_tags_allure(item)
                add_links_allure()
                # add description to allure report
                Context.test_result.description = Context.test_result.name

import os
import yaml
import logging
from allure_commons.model2 import Link, Label
from allure_commons.types import LinkType, LabelType


class Context:
    """
    Class to store and manage global settings used by the tests.
    This class provides a centralized location to store and access global settings
    that are used across multiple test cases.
    """
    pass


def expanded_raise_for_status(response):
    """
    Check if the response status is not OK (i.e., not in the 2xx range).

    If the status is not OK, log details about the request and response.

    Parameters:
    - response (requests.Response): The HTTP response object to check.

    Returns:
    None
    """
    try:
        response.raise_for_status()
    except Exception as e:
        logging.error(f" Not an OK response: {e}")
        logging.error(f" Request body: {response.request.method} {response.request.body}")
        logging.error(f" Response body: {response.content}")


def load_yaml(file):
    """
    Load YAML data from a file and set as attributes of the Context class.

    Parameters:
    - file (str): The path to the YAML file.

    Returns:
    None
    """
    file = get_absolute_path(file_name=file)
    with open(file, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        for section_name, section_data in yaml_data.items():
            setattr(Context, section_name, section_data)


def get_absolute_path(file_name):
    """
    Get the absolute path of a file in the project directory.

    Parameters:
    - file_name (str): The name of the file.

    Returns:
    - str: The absolute path of the file.
    """
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.dirname(current_script_directory)
    return os.path.join(project_directory, file_name)


def add_tags_allure(item):
    """
    Add tags to the Allure report based on pytest markers.

    Parameters:
    - item: The pytest item object.

    Returns:
    None
    """
    # add tags to allure report
    if hasattr(Context.test_result, 'labels'):
        for marker in item.iter_markers():
            if marker.name == 'case_id':
                Context.case_ids = marker.args
                Context.test_result.labels.extend(
                    Label(name=LabelType.TAG, value=case_id) for case_id in Context.case_ids)
            else:
                Context.test_result.labels.append(Label(name=LabelType.TAG, value=marker.name))


def add_links_allure():
    """
    Add links to the Allure report based on test case IDs.

    Returns:
    None
    """
    # add links to allure report
    for case_id in Context.case_ids:
        link_to_tr = f"{Context.test_documentation_url}/index.php?/cases/view/{case_id}"
        Context.test_result.links.append(Link(type=LinkType.TEST_CASE, url=link_to_tr, name=link_to_tr))

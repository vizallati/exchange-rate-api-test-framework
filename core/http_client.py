import requests
from core.utils import expanded_raise_for_status


class HttpConnectionError(Exception):
    pass


class HttpClient:
    """Standard REST API client"""

    def __init__(self, ssl_verification=True):
        """
        Initialize the HttpClient.

        Parameters:
        - ssl_verification (bool): Whether to perform SSL certificate verification.
                                   Default is True.
        """
        self.session = requests.Session()
        self.session.verify = ssl_verification
        self.session.headers = {}

    def request(self, method, url, **kwargs):
        """
        Send an HTTP request.

        Parameters:
        - method (str): The HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
        - url (str): The URL to which the request is sent.
        - **kwargs: Additional keyword arguments to be passed to the requests.request method.

        Returns:
        requests.Response: The HTTP response object.

        Raises:
        HttpConnectionError: If a connection error occurs.
        """
        try:
            response = self.session.request(method, url, **kwargs)
            expanded_raise_for_status(response)
            return response
        except ConnectionError as e:
            raise HttpConnectionError('Exception has occurred: {}'.format(e))


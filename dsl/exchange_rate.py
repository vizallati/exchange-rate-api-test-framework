from core.http_client import HttpClient
from core.utils import Context


class ExchangeRate(HttpClient):
    """
    This class extends the HttpClient class to interact specifically with an exchange rate API.
    It provides methods to perform standard requests for exchange rates and pair conversions.

    Attributes:
    - base_url (str): The base URL of the exchange rate API.
    - api_version (str): The version of the exchange rate API.
    - api_key (str): The API key used to authenticate requests to the exchange rate API.
    """

    def __init__(self):
        """
        Initialize the ExchangeRate instance.
        Sets up the base URL, API version, and API key from the Context class.
        """
        super().__init__()
        self.base_url = Context.base_url
        self.api_version = Context.api_version
        self.api_key = Context.api_key

    def standard_requests(self, currency):
        return self.request('GET', f'{self.base_url}/{self.api_version}/{self.api_key}/latest/{currency}')

    def pair_conversions(self, input_currency, output_currency, amount):
        return self.request('GET', f'{self.base_url}/{self.api_version}/{self.api_key}/pair/{input_currency}/'
                                   f'{output_currency}/{amount}')

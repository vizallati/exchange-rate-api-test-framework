from core.http_client import HttpClient
from core.utils import Context


class ExchangeRate(HttpClient):
    """
    This class extends the HttpClient class to interact specifically with the exchange rate API.
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

    def standard_requests(self, currency, api_key=None):
        api_key = api_key or self.api_key
        return self.request('GET', f'{self.base_url}/{self.api_version}/{api_key}/latest/{currency}')

    def pair_conversions(self, input_currency, output_currency, amount, api_key=None):
        api_key = api_key or self.api_key
        url = f'{self.base_url}/{self.api_version}/{api_key}/pair/{input_currency}/{output_currency}'
        if amount:
            url += f'/{amount}'
        return self.request('GET', url)


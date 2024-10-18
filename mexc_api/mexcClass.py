import requests
import hmac
import hashlib
from requests.exceptions import RequestException
from mexc_api import conf
config = conf()
class TOOL(object):
    def __init__(self):
        self.base_uri = config.mexc_host
        self.api_key = config.api_key
        self.secret_key = config.secret_key
    def _get_timestamp(self):
        try:
            response = requests.get(f'{self.base_uri}/api/v3/time')
            response.raise_for_status()
            return response.json()['serverTime']
        except RequestException as e:
            print(f"HTTP time request failed: {e}")
            return False
    def _signature(self, parameters):
        parameters['timestamp'] = self._get_timestamp()
        query_string = "&".join([f"{key}={value}" for key, value in parameters.items()])
        secret_key = self.secret_key
        signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        parameters['signature'] = signature
        query_parameters = parameters
        return query_parameters
    def _request(self,query_parameters,route):
        base_uri = self.base_uri
        headers = {
            'X-MEXC-APIKEY': self.api_key
        }
        try:
            response = requests.post(f'{base_uri}{route}', params=query_parameters, headers=headers)
            response.raise_for_status()
            print(response.json())
        except RequestException as e:
            print(f"HTTP request failed: {e}")
            return False
class mexc_trade(TOOL):
    def post_order(self, params):
        sign = self._signature(params)
        self._request(sign, "/api/v3/order")
    # 1. Создание нового ListenKey
class mexc_trade(TOOL):
    def post_order(self, params):
        sign = self._signature(params)
        self._request(sign, "/api/v3/order")
    # 1. Создание нового ListenKey
    def create_listen_key(self):
        params = {'recvWindow': 5000}
        params['timestamp'] = self._get_timestamp()
        query_string = "&".join([f"{key}={value}" for key, value in params.items()])
        secret_key = self.secret_key
        signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        params['signature'] = signature
        print(params)
        USER_DATA_STREAM_ENDPOINT = "/api/v3/userDataStream"
        base_uri = self.base_uri
        headers = {
            'X-MEXC-APIKEY': self.api_key
        }
        response = requests.post(f"{base_uri}{USER_DATA_STREAM_ENDPOINT}", headers=headers,params=params)
        if response.status_code == 200:
            listen_key = response.json()['listenKey']
            print(f"New ListenKey created: {listen_key}")
            return listen_key
        else:
            print(f"Error creating ListenKey: {response.text}")
            return None



import json
import requests
import price_tracker_formatting as ptf

class Sets:
    crypto = 'BTC'
    currency = 'USD'
    url = f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms={currency}'

class GetResponse(Sets):
    @classmethod
    def get_response(cls):
        response = requests.get(cls.url).text
        formating_string = ptf.remove_special_char(response, 'USD:{}"')
        return formating_string
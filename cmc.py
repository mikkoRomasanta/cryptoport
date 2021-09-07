import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

headers = {
    'X-CMC_PRO_API_KEY' : api_key,
    'Accepts' : 'application/json'
}

#cmc ids of tokens
id = '1027,6490,8968,9218,8719,10408,6783,5824,11020,11130,11067,1839,11427'

params = {
    'id' : id
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def call_api():
    json = requests.get(url, params=params, headers=headers).json()
    coins = json['data']

    return coins


def get_quotes():
    coins = call_api()
    quotes = []
    for (index,coin) in coins.items():
        print(coin['symbol'],coin['quote']['USD']['price'])
        quotes.append([coin['symbol'],coin['quote']['USD']['price']])

    return quotes

def get_ids(sym):
    symbol = sym
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    params = {
        'symbol' : symbol
    }

    json = requests.get(url, params=params, headers=headers).json()
    coin_id = json['data'][symbol]['id']

    return coin_id


if __name__ == '__main__':
    print(get_ids('BMON'))
    # print(api_key)
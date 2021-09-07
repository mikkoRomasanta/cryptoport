import requests

contract = ['0x2ae9b69d191a6fc2088ec28f207d40b3fa67cd82','0x339c72829ab7dd45c3c52f965e7abe358dd8761e','0x6652462466DCeE5Cb1dda95379FaE3c3E57f6719','0xd7730681b1dc8f6f969166b29d8a5ea8568616a3']
url = 'https://api.pancakeswap.info/api/v2/tokens/'
quotes = []

def call_api(index):
    json = requests.get(url+contract[index]).json()
    return json

def get_quotes():
    for index,coin in enumerate(contract):
        result = call_api(index)
        quotes.append([result['data']['symbol'],result['data']['price']])
        print(result['data']['symbol'],result['data']['price'])

    return quotes
        

if __name__ == '__main__':
    print(get_quotes())
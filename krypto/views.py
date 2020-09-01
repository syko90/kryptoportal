from django.shortcuts import render
import requests
import json
from web3 import Web3



def home(request):
    # aktualne kursy krypto
    
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT,IOT&tsyms=PLN,EUR")
    price = json.loads(price_request.content)

    # aktualne wydarzenia
    url = "https://developers.coinmarketcal.com/v1/events"
    querystring = {"max":"1", "translations": "pl"}
    payload = ""
    headers = {
    'x-api-key': "WunvIC33Xd7vXPOhnsQAW5Whpscqw2oB8bgMypCk",
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    event_cal = json.loads(response.content)
    


    # krypto widomości
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price, 'event_cal': event_cal}) 


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        krypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=PLN,EUR")
        krypto = json.loads(krypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'krypto': krypto})
    else:     
        return render(request, 'prices.html', )

def wallet(request):
    infura_url = "https://mainnet.infura.io/v3/1b8ab038ffe14a658bf6d01b7f24ba97"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    is_connected = web3.isConnected()
    gas_price = web3.eth.gasPrice # zwraca cenę gazu w Wei

    eth_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=PLN")
    ethereum = json.loads(eth_request.content)
    # print(type(ethereum['RAW']['ETH']['PLN']['PRICE']))  # just check price of ETH

    balance = web3.eth.getBalance("0x3cA0Cf35ca066eD617774f393Bfb3085a340296B")
    balance_eth = web3.fromWei(balance, "ether")
    #print(balance_eth*ethereum['RAW']['ETH']['PLN']['PRICE'])
    balance_pln = float(balance_eth)*float(ethereum['RAW']['ETH']['PLN']['PRICE'])
    return render(request, 'wallet.html', {'is_connected': is_connected, 'gas_price': gas_price, 'balance_eth': balance_eth, 'balance_pln': balance_pln, 'ethereum': ethereum})

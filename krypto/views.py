from django.shortcuts import render
import requests
import json

def home(request):
    # aktualne kursy krypto
    
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BAT,IOT&tsyms=PLN,EUR")
    price = json.loads(price_request.content)


    # krypto waidomości
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price}) 

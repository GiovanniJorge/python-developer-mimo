import requests
import os

api_key = os.getenv("MIMO_CRYPTO_CRAZE_API_KEY")
headers = {"api-key": api_key}

def get_crypto_price(coin_id):
    url = f"https://crypto-craze.mimo.dev/api/coins/{coin_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def print_crypto_price(crypto):
    symbol = crypto.get("symbol")
    price_usd = crypto.get("priceUsd")
    print(symbol)
    print(price_usd)

crypto = get_crypto_price("bitcoin")
print_crypto_price(crypto)

crypto = get_crypto_price("ethereum")
print_crypto_price(crypto)

crypto = get_crypto_price("solana")
print_crypto_price(crypto)
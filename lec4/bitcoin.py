import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    fl = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    pass
except ValueError:
    print("Command-line argument is not a number")

price = response["bpi"]["USD"]["rate_float"]
amount = fl * price
print(f"${amount:,.4f}")

import requests
from pprint import pprint

x = requests.get("https://github.com/")

pprint(x.content)
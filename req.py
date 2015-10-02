import requests
import json

r = requests.get('http://localhost:8888/ttdata.json')

jsonParsed = r.json()

array = jsonParsed["data"]

for x in array:
	print x["event_name"]

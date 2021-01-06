import requests

r = requests.get('http://localhost:5000/config')
print("config => ", r.json())

r = requests.get('http://localhost:5000/saco')
print("saco => ", r.json())


r = requests.get('http://localhost:5000/fisga')
print("figa => ", r.json())


r = requests.get('http://localhost:5000/linha')
print("linha => ", r.json())
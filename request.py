import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'size':0, 'bed':1, 'Orientation':2})

print(r.json())
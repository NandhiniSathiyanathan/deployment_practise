import requests
data_to_be_sent = {
        'sl' : '1.2',
        'sw' : '0.1',
        'pl' : '0.3',
        'pw' : '1.5'

    }

url = ''

response = requests.post(data = data_to_be_sent, url = url)

if response.status_code == 200:
   print(response.text)
else:
   print(response.status_code)
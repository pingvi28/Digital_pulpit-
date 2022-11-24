import requests


# author: Kashapova Dilyara

ip = str(input('Введите ip: '))
response = requests.get('http://ip-api.com/json/' + ip)
data = response.json()

if data.get('status') == 'success':
    print(data.get('country'))
else:
    print('Такого ip не существует')

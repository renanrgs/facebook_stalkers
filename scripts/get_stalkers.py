import requests
import re
import os

cookies = {
    'datr': os.environ.get('FACEBOOK_DATR')
}

headers = {
    'accept': os.environ.get('FACEBOOK_ACCEPT')
}

data = {
    'lsd': os.environ.get('FACEBOOK_LSD'),
    'email': os.environ.get('EMAIL'),
    'encpass': os.environ.get('FACEBOOK_ENCPASS')
}

response = requests.post('https://www.facebook.com/login/', cookies=cookies, headers=headers, data=data)
stalkers = re.findall('"buddy_id":"(\\d*)".*?"name":(".*?")', str(response.content))

for stalker in stalkers:
    print(f'{stalker[1]} - https://www.facebook.com/{stalker[0]}')


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

for stalker_id, stalker_name in stalkers:
    print(f'{stalker_name} - https://www.facebook.com/{stalker_id}')

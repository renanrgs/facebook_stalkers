import requests
import re
import os


def get_stalkers():
    cookies = {
        'c_user': os.environ['FACEBOOK_USER_ID'],
        'xs': os.environ['FACEBOOK_XS'],
    }

    headers = {
        'accept': os.environ['FACEBOOK_ACCEPT']
    }

    data = {
        'lsd': os.environ['FACEBOOK_LSD'],
        'email': os.environ['EMAIL'],
        'encpass': os.environ['FACEBOOK_ENCPASS']
    }

    response = requests.post('https://www.facebook.com/login/', cookies=cookies, headers=headers, data=data)
    stalkers = re.findall('"buddy_id":"(\\d*)".*?"name":(".*?")', str(response.content))

    for stalker_id, stalker_name in stalkers:
        print(f'{stalker_name} - https://www.facebook.com/{stalker_id}')


if __name__ == '__main__':
    get_stalkers()

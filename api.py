import requests
URL = 'https://pkob268954.herokuapp.com/api/'


def get_victim_info(ic, phone):
    response = requests.post(url=URL+'victim_info', json={
        'ic': ic,
        'phone': phone
    })
    payload = response.json()
    if(response.status_code != 200 and payload['status'] == 'failed'):
        return None

    data = payload['data']
    return data

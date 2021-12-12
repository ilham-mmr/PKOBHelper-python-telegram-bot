import requests
URL = 'http://127.0.0.1:8000/api/'


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

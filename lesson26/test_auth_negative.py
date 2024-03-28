from lesson26.auth_session_negative import url_for_auth, auth_info
import requests
import pytest
import json
from requests.auth import HTTPBasicAuth
auth_info_corrupted = ('user', 'passwd1')
url_for_bearer = 'https://reqres.in/'
auth_for_bearer = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}



def test_attempt_to_auth():

    response = requests.get(url_for_auth, auth=auth_info_corrupted)
    assert response.json()['user'] == 'user'


def test_attempt_to_login_negative():
    try:
        response = requests.get(url_for_auth, auth=auth_info_corrupted)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 401:
            pass
        else:
            raise err


def test_pick_one_item_with_bearer_token():
    with requests.Session() as session:
        login_response = session.post('https://reqres.in/api/register', data=auth_for_bearer)
        bearer = login_response.json()['token']
        headers = {'Authorization': f'Bearer {bearer}'}
        single_user_response = session.get(url_for_bearer + 'api/users/2', headers=headers)


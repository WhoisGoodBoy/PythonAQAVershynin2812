import requests
from requests.auth import HTTPBasicAuth

url_for_session = 'https://restful-booker.herokuapp.com/booking/1744'
url_for_auth = 'https://httpbin.org/basic-auth/user/passwd'
auth_info = ('user', 'passwd')

def call_session():
    with requests.Session() as session:
        unknown_result = session.get(url_for_session)
        print(unknown_result.json())
        return unknown_result

def auth_basic_example():
    response = requests.get(url_for_auth, auth=auth_info)
    return response.json()


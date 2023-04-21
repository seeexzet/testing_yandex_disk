import requests
from ya_token import TOKEN
from unittest import TestCase

class TestUpload(TestCase):
    def test_upload(self):
        res = upload('new_folder')
        self.assertIn(res, [200, 201])
        res = upload('new_folder')
        self.assertEqual(res, 409)
        res = upload('///')
        self.assertEqual(res, 404)

def get_headers(token):
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN}'
    }

def upload(folder_name):
    base_host = 'https://cloud-api.yandex.net:443/'
    uri_create_folder = 'v1/disk/resources'
    request_url_create_folder = base_host + uri_create_folder
    params1 = {'path': folder_name, 'overwrite': True}
    responce = requests.put(request_url_create_folder, headers=get_headers(TOKEN), params=params1)
    print(responce.status_code)
    return responce.status_code


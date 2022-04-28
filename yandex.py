import requests


class YaUploader:

    def __init__(self, ya_token, folder_name):
        self.ya_token = ya_token
        self.folder_name = folder_name
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.ya_token}'
        }

    def create_folder(self):
        params = {
            'path': self.folder_name
        }
        response = requests.put(self.url, params=params, headers=self.headers)
        return response.status_code




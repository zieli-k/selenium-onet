import requests


class Service:
    def __init__(self, endpoint, url):
        self.url = endpoint + url

    def get_request(self, headers=None):
        return requests.get(self.url, headers=headers).json()

    def post_request(self, headers=None, data=None):
        return requests.post(self.url, headers=headers, data=data).json()


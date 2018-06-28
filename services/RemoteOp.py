import requests

class RemoteOp:
    def __init__(self):
        pass

    def get_remote_data(self, url):
        return requests.get(url)
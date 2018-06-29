import requests

class RemoteOp:
    def __init__(self):
        pass

    def fetch_data(self):
        print('CALLED ACTUAL METHOD')
        return requests.get('https://jsonplaceholder.typicode.com/posts/1')
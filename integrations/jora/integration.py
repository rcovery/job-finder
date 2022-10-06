from requests import get

class Jora:
    url = 'jora.com'
    region = 'us'

    predefined_regions = ['us', 'ca', 'br', 'uk', 'pt']

    def __init__(self, search, location):
        self.search = search
        self.location = location

    def get_results(self):
        get(f'https://{self.region}.{self.url}/j?q={self.search}&l={self.location}')
        
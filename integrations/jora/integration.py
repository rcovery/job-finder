from requests import get

class Jora:
    url = 'jora.com'
    region = 'us'
    search = ''
    location = ''

    predefined_regions = ['us', 'ca', 'br', 'uk', 'pt']

    # def __init__(self):

    # def get_results(self, region, search = '', location = ''):
    #     if (region == '*'):

    def request(self):
        get(f'https://{self.region}.{self.url}/j?q={self.search}&l={self.location}')
        
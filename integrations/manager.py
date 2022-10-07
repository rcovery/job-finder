from .jora import Jora

class Manager:
    def __init__(self, integration = 'jora'):
        match (integration):
            case 'jora':
                pass
            case _:
                self.instance = Jora()

    def get(self):
        self.instance.request()

    @property
    def region(self, region = 'us'):
        self.instance.region = region
from .jora import Jora

class Manager:
    def __init__(self, integration = 'jora'):
        self.integration = integration

        if (integration == 'jora'):
            self.instance = Jora()
        else:
            self.instance = Jora()

    def get(self, search = None, region = None, location = None):
        if (search):
            self.instance.search = search

        if (region):            
            self.instance.region = region

        if (self.integration == 'jora'):
            if (location):
                self.instance.location = location

        return self.instance.get_results()

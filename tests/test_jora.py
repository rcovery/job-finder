from unittest import TestCase
from integrations.manager import Manager

class TestJoraIntegration(TestCase):
    def test_response(self):
        jora = Manager(integration = 'jora')
        
        response = jora.get()

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 3)

    def test_with_search(self):
        jora = Manager()
        
        response = jora.get(search = 'dev')

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 3)

    def test_with_region(self):
        jora = Manager()

        response = jora.get(region = 'ca')

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 3)

    def test_with_location(self):
        jora = Manager()

        response = jora.get(location = 'Silicon Valley')

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 3)

    def test_with_region_list(self):
        jora = Manager()

        response = jora.get(region = ['ca', 'pt'])

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 3)

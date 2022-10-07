from unittest import TestCase
from ..integrations.manager import Manager

class TestJoraIntegration(TestCase):
    def test_us_region(self):
        jora = Manager()

        jora.region = 'ca'
        
        jora.get()

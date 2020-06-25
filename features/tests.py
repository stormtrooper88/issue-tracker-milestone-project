from django.test import TestCase
from .models import Features

# Create your tests here.
class ProductTest(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Features models
    """

    def test_str(self):
        test_name = Features(name='A feature')
        self. assertEqual(str(test_name), 'A feature')